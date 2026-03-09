from typing import TypedDict, List
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    values: List[int]
    name: str
    result: str

def process_values(state: AgentState) -> AgentState:
    print(state)
    state['result'] = 'Hi ' + state['name'] + '! Your sum is: ' + str(sum(state['values']))
    return state

graph = StateGraph(AgentState)
graph.add_node('processor', process_values)
graph.set_entry_point('processor')
graph.set_finish_point('processor')
app = graph.compile()

answer = app.invoke({'name': 'Sundar', 'values': [1,2,3,4]})
print(answer)
print(answer['result'])

from IPython.display import display, Image
display(Image(app.get_graph().draw_mermaid_png()))