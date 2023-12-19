import sys

input = open(sys.argv[1]).read()

workflows_text, parts_text = input.strip().split("\n\n")

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
workflows[in_index].append({'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)})

result = 0
while not all(len(x) == 0 for x in workflows):
    i = 0
    while len(workflows[i]) == 0:
        i += 1

    part = workflows[i].pop()
    for rule in workflow_rules[i]:
        leftover_range = {}
        sent_range = {}

        if isinstance(rule[0], bool):
            leftover_range = {'x': 0, 'm': 0, 'a': 0, 's': 0}
            sent_range = part
        elif rule[0][1] == '<':
            for key, value in part.items():
                if key == rule[0][0]:
                    sent_range[key] = (value[0], min(value[1], rule[0][2] - 1))
                    leftover_range[key] = (max(value[0], rule[0][2]), value[1])
                else:
                    sent_range[key] = value
                    leftover_range[key] = value
        elif rule[0][1] == '>':
            for key, value in part.items():
                if key == rule[0][0]:
                    sent_range[key] = (max(value[0], rule[0][2] + 1), value[1])
                    leftover_range[key] = (value[0], min(value[1], rule[0][2]))
                else:
                    sent_range[key] = value
                    leftover_range[key] = value

        part = leftover_range

        if rule[1] == 'A':
            temp = 1
            for x in sent_range.values():
                temp *= max(x[1] - x[0] + 1, 0)
            result += temp
        elif rule[1] == 'R':
            pass
        else:
            new_workflow_idx = workflow_ids[rule[1]]
            workflows[new_workflow_idx].append(sent_range)
    pass

print(result)
