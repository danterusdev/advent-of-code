import sys

input = open(sys.argv[1]).read()

workflows_text, parts_text = input.strip().split("\n\n")

parts = []

for line in parts_text.split("\n"):
    line = line[1:-1]
    part = {}
    for attr in line.split(","):
        key, value = attr.split("=")
        part[key] = int(value)

    parts.append(part)

workflow_ids = {}
workflows = []
workflow_rules = []

i = 0
for line in workflows_text.split("\n"):
    name = line[0:line.index("{")]
    workflow_ids[name] = i
    i += 1
    rules_text = [x for x in line[line.index("{") + 1: line.index("}")].split(",")]
    # condition, action or action
    rules = []
    for rule_text in rules_text:
        if ":" in rule_text:
            condition, result = rule_text.split(":")
            sign_index = condition.index("<") if "<" in rule_text else condition.index(">")
            assert sign_index != -1
            rules.append(((condition[0:sign_index], condition[sign_index], int(condition[sign_index + 1:])), result))
        else:
            rules.append((True, rule_text))

    workflows.append([])
    workflow_rules.append(rules)

in_index = workflow_ids["in"]
for part in parts:
    workflows[in_index].append(part)

def rule_matches(rule, part):
    if isinstance(rule[0], bool):
        return True

    if rule[0][1] == '<':
        return part[rule[0][0]] < rule[0][2]

    if rule[0][1] == '>':
        return part[rule[0][0]] > rule[0][2]

result = 0
while not all(len(x) == 0 for x in workflows):
    i = 0
    while len(workflows[i]) == 0:
        i += 1

    part = workflows[i].pop()
    for rule in workflow_rules[i]:
        if rule_matches(rule, part):
            break

    if rule[1] == 'A':
        # accepted
        for x in part.values():
            result += x
        pass
    elif rule[1] == 'R':
        # rejected
        pass
    else:
        new_workflow_idx = workflow_ids[rule[1]]
        workflows[new_workflow_idx].append(part)
    pass

print(result)
