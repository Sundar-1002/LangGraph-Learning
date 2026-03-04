from langgraph.graph import StateGraph
from typing import TypedDict, List

class AgentState(TypedDict):
    name : str
    age : int
    skill : List[str]
    result : str

def greet(state: AgentState) -> AgentState:
    state['result'] = 'Hello ' + state['name'] + '! '
    return state

def describe(state: AgentState) -> AgentState:
    state['result'] = state['result'] + 'You are ' + str(state['age']) + ' years old. '
    return state

def list_skills(state: AgentState) -> AgentState:
    state['result'] = state['result'] + ' You have skills in '
    for skill in range(len(state['skill'])):
        if skill == len(state['skill']) - 1:
            state['result'] = state['result'] + state['skill'][skill] + '.'
        elif skill == len(state['skill']) - 2:
            state['result'] = state['result'] + state['skill'][skill] + ' and '
        else:
            state['result'] = state['result'] + state['skill'][skill] + ', '
    return state

app = StateGraph(AgentState)
app.add_node('greet', greet)
app.add_node('describe', describe)
app.add_node('list_skills', list_skills)
app.set_entry_point('greet')
app.add_edge('greet', 'describe')
app.add_edge('describe', 'list_skills')
app.set_finish_point('list_skills')
graph = app.compile()

answer = graph.invoke({'name': 'Sundar', 'age': 25, 'skill': ['Python', 'JavaScript', 'C++']})
print(answer)
print(answer['result'])