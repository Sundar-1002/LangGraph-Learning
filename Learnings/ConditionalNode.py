from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class AgentState(TypedDict):
    number1: int
    number2: int
    number3: int 
    number4: int
    operation1: str
    operation2: str
    finalnumber: int
    finalnumber2: int

def add_node1(state: AgentState) -> AgentState:
    state['finalnumber'] = state['number1'] + state['number2']
    return state

def add_node2(state: AgentState) -> AgentState:
    state['finalnumber2'] = state['number3'] + state['number4']
    return state

def sub_node1(state: AgentState) -> AgentState:
    state['finalnumber'] = state['number1'] - state['number2']
    return state

def sub_node2(state: AgentState) -> AgentState:
    state['finalnumber2'] = state['number3'] - state['number4']
    return state

def conditional_node(state: AgentState) -> AgentState:
    if state['operation1'] == '+':
        return 'addition1'
    elif state['operation1'] == '-':
        return 'subtraction1'
    
def conditional_node2(state: AgentState) -> AgentState:
    if state['operation2'] == '+':
        return 'addition2'
    elif state['operation2'] == '-':
        return 'subtraction2'
    
graph = StateGraph(AgentState)
graph.add_node('addition1', add_node1)
graph.add_node('addition2', add_node2)
graph.add_node('subtraction1', sub_node1)
graph.add_node('subtraction2', sub_node2)
graph.add_node('conditional1', lambda state: state)
graph.add_node('conditional2', lambda state: state)

graph.add_edge(START, 'conditional1')
graph.add_conditional_edges('conditional1',
                            conditional_node,
                            {
                                'addition1': 'addition1',
                                'subtraction1': 'subtraction1'
                            })
graph.add_edge('addition1', 'conditional2')
graph.add_edge('subtraction1', 'conditional2')
graph.add_conditional_edges('conditional2',
                            conditional_node2,
                            {
                                'addition2': 'addition2',
                                'subtraction2': 'subtraction2'
                            })
graph.add_edge('addition2', END)
graph.add_edge('subtraction2', END)
app = graph.compile()

initial_state = AgentState(number1 = 5, number2= 5, number3= 10, number4 = 5, operation1='+', operation2='-')
final_state = app.invoke(initial_state)
print(final_state)
print(final_state['finalnumber'], final_state['finalnumber2'])