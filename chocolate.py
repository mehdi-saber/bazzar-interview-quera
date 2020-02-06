from queue import PriorityQueue


def chocolate():
    n = int(input())
    in_str=input()
    boxes = [*map(int, in_str.split())]

    # in_str = "1 6 2 5 3 7"
    # boxes = [*map(int, in_str.split())]
    # n = len(boxes)

    if sum(boxes) % n != 0:
        return -1
    mean = sum(boxes) // n
    min_heap = PriorityQueue()
    for box_i, box in enumerate(boxes):
        min_heap.put((box, box_i))

    steps = 0
    min_box, min_box_i = min_heap.get()
    while min_box < mean:
        increment = mean - min_box
        r = 0
        while increment > 0:
            for direction in [-1, 1]:
                if 0 <= min_box_i + r * direction < n:
                    if boxes[min_box_i + r * direction] > mean:
                        decrement = min(boxes[min_box_i + r * direction] - mean, increment)
                        boxes[min_box_i + r * direction] -= decrement
                        boxes[min_box_i] += decrement
                        increment -= decrement
                        steps += r * decrement
            r += 1
        min_box, min_box_i = min_heap.get()
    return steps


if __name__ == '__main__':
    print(chocolate())