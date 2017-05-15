from fsm import FiniteStateMachine


# start -> programming_state | error_state
def start_transitions(txt):
    split_text = txt.split(None, 1)
    word, txt = split_text if len(split_text) > 1 else (txt, "")
    if word == "Programming":
        new_state = "programming_state"
    else:
        new_state = "error_state"
    return new_state, txt


# programming_state -> is | error_state
def programming_state_transitions(txt):
    split_text = txt.split(None, 1)
    word, txt = split_text if len(split_text) > 1 else (txt, "")
    if word == "is":
        new_state = "is_state"
    else:
        new_state = "error_state"
    return new_state, txt


# is_state -> not_state | pos_state | neg_state | error_state
def is_state_transitions(txt):
    split_text = txt.split(None, 1)
    word, txt = split_text if len(split_text) > 1 else (txt, "")
    if word == "not":
        new_state = "not_state"
    elif word in positive:
        new_state = "pos_state"
    elif word in negative:
        new_state = "neg_state"
    else:
        new_state = "error_state"
    return new_state, txt


# not_state -> neg_state | pos_state | error_state
def not_state_transitions(txt):
    split_text = txt.split(None, 1)
    word, txt = split_text if len(split_text) > 1 else (txt, "")
    if word in positive:
        new_state = "neg_state"
    elif word in negative:
        new_state = "pos_state"
    else:
        new_state = "error_state"
    return new_state, txt


positive = ["great", "super", "fun", "entertaining", "easy", "awesome"]
negative = ["boring", "difficult", "ugly", "bad", "strange"]

if __name__ == "__main__":
    m = FiniteStateMachine()

    m.add_state("start_state", start_transitions)
    m.add_state("programming_state", programming_state_transitions)
    m.add_state("is_state", is_state_transitions)
    m.add_state("not_state", not_state_transitions)
    m.add_state("neg_state", None, end_state=1)
    m.add_state("pos_state", None, end_state=1)
    m.add_state("error_state", None, end_state=1)

    m.set_start("start_state")

    m.run("Programming is great")
    m.run("Programming is very great")
    m.run("Programming is difficult")
    m.run("Programming is not boring")
    m.run("Math is strange")
