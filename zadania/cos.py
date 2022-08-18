# lista = [[1,2,3], [4, 5, 6], [7, 8, 9]]
# sum_ = 0
# for list_ in lista:
#     # sum_ += sum(list_)
#     for element in list_:
#         sum_ += element
# print(sum_)

if __name__ == '__main__':
    records = []
    def take_second(elem):
        return elem[1]
    def print_first(elem):
        return elem[0]

    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append((name, score))
    # sorted_records_by_value = records.sort(key=take_second)
    records.sort(key=take_second)
    print(len(records))
    # for element in range(1, len(records)):
    #     print(element)
    print(records)
