import random
import datetime

NUM_OF_TRIALS = 5
NUM_OF_ALL_CHARS = 10
NUM_OF_ABS_CHARS = 2

def main():
    st = datetime.datetime.now()
    for _ in range(NUM_OF_TRIALS):
        seikai = shutsudai()
        f = kaitou(seikai)
        if (f == 1):
            break
    ed = datetime.datetime.now()
    print(f"所要時間：{(ed-st).seconds}秒かかりました")


def shutudai():
    alphabets = [chr(c+65) for c in range(26)]
    all_char_lst = random.sample(alphabets, NUM_OF_ALL_CHARS)
    print(f"対象文字：{all_char_lst}")
    
    abs_char_lst = random.sample(all_char_lst, NUM_OF_ABS_CHARS)
    print(f"欠損文字：{abs_char_lst}")

    pre_char_lst = [c for c in all_char_lst if c not in abs_char_lst]
    print(f"表示文字：{pre_char_lst}")

    return abs_char_lst


def kaitou(seikai):
    num = int(input("欠損文字はいくつあるでしょうか？"))
    if num != NUM_OF_ABS_CHARS:
        print("不正解です")
        print("-"*50)
        return 0
    else:
        print("正解です. それでは具体的に欠損文字を1つずつ入力してください")
        for i in range(NUM_OF_ABS_CHARS)
            c = input(f"{i+1}つ目の文字を入力して下さい：")
            if c not in seikai:
                print("不正解です.またチャレンジしてください")
                print("-"*50)
                return 0
            seikai.remove(c)
        return 1


if __name__ == "__main__":
    main()