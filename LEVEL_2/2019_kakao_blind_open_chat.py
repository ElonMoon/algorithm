def solution(records):
    user_list = {}
    action_list = []
    answer = []
    for record in records:
        data = record.split(' ')
        if data[0] in ('Enter', 'Change'):
            user_list[data[1]] = data[2]
        action_list.append((data[0], data[1]))

    for action, user in action_list:
        if action == 'Enter':
            answer.append(f'{user_list[user]}님이 들어왔습니다.')
        elif action == 'Leave':
            answer.append(f'{user_list[user]}님이 나갔습니다.')

    return answer
