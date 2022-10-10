# -*- coding: utf-8 -*-
import csv
import string


class Message:
    def __init__(self, class_label, message, spam_words, length, symbols, links):
        self.class_label = class_label
        self.message = message
        self.spam_words = spam_words
        self.length = length
        self.symbols = symbols
        self.links = links

    def getClassLabel(self):
        return self.nature

    def getMessage(self):
        return self.message

    def getDoesHaveSpammyWords(self):
        return self.spam_words

    def getLength(self):
        return self.length

    def getNumberOfSymbols(self):
        return self.symbols

    def getDoesHaveLinks(self):
        return self.links


def doesHaveLinks(list_links, message):
    for link in list_links:
        if link in message:
            return True
    return False


def doesHaveSpammyWords(list_spamwords, message):
    split_message = message.split(" ")
    for word in list_spamwords:
        if word in split_message:
            return True
    return False


def lengthOfText(message):
    return len(message)


def numberOfSymbols(message):
    count = 0
    all_punctuation = string.punctuation
    for letter in message:
        if letter in all_punctuation:
            count += 1
    return count


def writingToCSV(file_name, lines):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)


def make_predictions(message):
    spam_words = message.getDoesHaveSpammyWords()
    symbols = message.getNumberOfSymbols()
    links = message.getDoesHaveLinks()
    length = message.getLength()

    if length <= 99:
        if links == True:
            if length <= 71:
                return "ham"
            else:
                return "spam"
        else:
            if spam_words == False:
                return "ham"
            else:
                if length <= 41:
                    return "ham"
                else:
                    if symbols <= 9:
                        if length <= 46:
                            return "ham"
                        else:
                            return "spam"
                    else:
                        if length <= 68:
                            return "ham"
                        else:
                            if symbols <=17:
                                if symbols <= 12:
                                    return "spam"
                                else:
                                    return "ham"
                            else:
                                return "ham"
    else:
        if spam_words == True:
            if symbols > 38:
                return "ham"
            else:
                if length <= 127:
                    if symbols > 26:
                        return "ham"
                    else:
                        if symbols <= 21:
                            return "spam"
                        else:
                            if length <= 119:
                                return "ham"
                            else:
                                return "spam"
                else:
                    if symbols <= 30:
                        return "spam"
                    else:
                        if length > 148:
                            return "spam"
                        else:
                            if length > 147:
                                return "ham"
                            else:
                                if length > 136:
                                    return "spam"
                                else:
                                    return "ham"
        else:
            if links == True:
                if symbols <= 36:
                    return "spam"
                else:
                    if symbols <= 38:
                        return "spam"
                    if symbols > 38:
                        return "ham"
            else:
                if symbols > 41:
                    return "ham"
                else:
                    if length <= 131:
                        return "ham"
                    else:
                        if symbols <= 36:
                            if length > 152:
                                if length > 162:
                                    return "ham"
                                else:
                                    if symbols > 27:
                                        return "spam"
                                    else:
                                        return "ham"
                            else:
                                if symbols > 31:
                                    return "ham"
                                else:
                                    if symbols > 30:
                                        return "spam"
                                    else:
                                        return "ham"
                        else:
                            if length > 164:
                                return "ham"
                            else:
                                if length <= 156:
                                    return "spam"
                                else:
                                    if length <= 158:
                                        return "ham"
                                    else:
                                        if symbols > 40:
                                            return "spam"
                                        else:
                                            if symbols > 39:
                                                return "ham"
                                            else:
                                                return "spam"




def main():
    count_good = 0
    count = 0
    list_links = ["http", "www", "::", "//", ":", ".com", ".uk", ".biz", "https", ".net", ]
    list_spamwords = ["spam", "click", "call", "text", "free", "press", "award", "prize", "txt", "claim", "guaranteed",
                      "urgent", "private", "win", "won", "ansr", "rcv", "svc", "go", "stop", "msg", "join", "reply",
                      "unsubscribe", "charge", "entitled", "send", "congrats", "collect", "activate", "congratulations",
                      "unsub", "xclusive", "chat", "offer", "expire", "get", "sms", "forwarded", "alert", "vary",
                      "charges", "subscribe", "unclaimed", "unsub", "visit", "opt out", "new", "trial", "redeemed",
                      "redeem", "content", "download", "chat", "winner"]
    features_list = [["doesHaveLinks", "doesHaveSpammyWords", "lengthOfText", "numberOfSymbols", "Class Label"]]
    with open('spam.csv', 'r', encoding="ISO-8859-1") as in_file:
        csv_reader = csv.reader(in_file, delimiter=',')
        header_row = next(csv_reader)
        predictions = list()
        for row in csv_reader:
            count += 1
            features_row = list()
            links = doesHaveLinks(list_links, row[1].lower())
            spam_words = doesHaveSpammyWords(list_spamwords, row[1].lower())
            symbols = numberOfSymbols(row[1].lower())
            length = lengthOfText(row[1].lower())
            class_label = row[0].lower()
            message = Message(row[0], row[1], spam_words, length, symbols, links)
            features_row.append(links)
            features_row.append(spam_words)
            features_row.append(symbols)
            features_row.append(length)
            features_row.append(class_label)
            features_list.append(features_row)

            prediction = make_predictions(message)
            predictions.append(prediction)
            print(prediction, class_label)
            if prediction == class_label:
                count_good += 1
    writingToCSV('features.arff', features_list)
    print(count_good, count, count_good/count)



main()
