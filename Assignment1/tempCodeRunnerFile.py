sum(matrix,[]))
# def sub_word(input_value):
   
def rot_word_left(word):
    return word[1:]+word[0]
# def subWord(temp):
def transpose(input_list):
    transposed_list = [
        ((input_list[i] >> (24 - 8 * j)) & 0xFF) << (8 * i) for i in range(4) for j in range(4)
    ]
    input_list[:] = transposed_list