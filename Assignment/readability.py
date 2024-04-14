def main():
    text = input("Text: ")
    count_letters = count_sentences = 0
    count_words = 1
    for i in text:
        if i.lower() in ['a','b','c','d','e','f','g','h','i','j','k',\
        'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
            count_letters += 1
    for i in text:
        if i in ['.','!','?']:
            count_sentences += 1
    for i in text:
        if i == ' ':
            count_words += 1
    l = count_letters*100/count_words
    s = count_sentences*100/count_words
    index = round(0.0588*l-0.296*s-15.8)
    if 1 <= index <= 16:
        print(f'grade{index}')
    elif index < 1 :
        print('before grade 1')
    else:
        print('grade 16+')

if __name__== "__main__":
    main()
