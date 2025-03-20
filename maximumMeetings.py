def maximumMeetings(meeting_effectiveness_scores):
    # we sort the input list first.
    # since each value is positive or negative, and will be added together
    # we can simply add the values as they are in a descending order list
    # until we reach the end of the list, or a negative value
    sorted_effectiveness_scores = sorted(meeting_effectiveness_scores, reverse=True)

    # the effectiveness index starts off at zero
    # the effectivness index must stay positive
    effectiveness_index = 0

    # we establish a counter for how many meetings are necessary
    maximum_meetings = 0

    for effectiveness_score in sorted_effectiveness_scores:
        effectiveness_index += effectiveness_score
        if effectiveness_index < 0:
            break
        maximum_meetings += 1

    return maximum_meetings

effectivness_input_test_cases = [
        [1, -20, 3, -2], 
        [4, -5, 20, 25, -26, -10],
        [3, -5, 6, -4, 10, -11],
        [7, 4, -12, 2, -1, 8, -3, -3],
        [6, -7, 1, -1],
        [5, -6],
        [5, -7, 1]
    ]

for test_case in effectivness_input_test_cases: 
    maximum_meetings = maximumMeetings(test_case)
    print("For the following meeting effectiveness scores: ", test_case)
    print("The maximum amount of meetings before a negative meeting effectivess index is: ", maximum_meetings, " meetings.")