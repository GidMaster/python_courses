"""
Refactoring
"""
"""
BAD_CODE

def responses_creator(item_ids):
    item_ids = [None] if item_ids is None else item_ids

    responses = []
    for item_id in item_ids:
        new_response = dict(item_id=item_id)
        responses.append(new_response)
    return responses

"""

def responses_creator(item_ids):

    if item_ids is None:
        return [{'item_id': None}]
    return [{'item_id': item_id} for item_id in item_ids]

def main():

    assert responses_creator([1,2,3]) == [{'item_id': 1}, {'item_id': 2}, {'item_id': 3}]
    assert responses_creator(None) == [{'item_id': None}]

if __name__ == '__main__':
    main()