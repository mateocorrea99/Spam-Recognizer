# -*- coding: utf-8 -*-
import csv
import string


# Creating Message class.
class Message:
    def __init__(self, class_label, text, spam_words, length, symbols, links):
        self.class_label = class_label
        self.message = text
        self.spam_words = spam_words
        self.length = length
        self.symbols = symbols
        self.links = links

    def getClassLabel(self):
        return self.class_label

    def getText(self):
        return self.text

    def getDoesHaveSpammyWords(self):
        return self.spam_words

    def getLength(self):
        return self.length

    def getNumberOfSymbols(self):
        return self.symbols

    def getDoesHaveLinks(self):
        return self.links


# Function to find if message has links or not.
def doesHaveLinks(list_links, message):
    for link in list_links:
        if link in message:
            return True
    return False


# Function to find if message has spam words or not.
def doesHaveSpammyWords(list_spamwords, message):
    split_message = message.split(" ")
    for word in list_spamwords:
        if word in split_message:
            return True
    return False


# Function to find the length of the text.
def lengthOfText(text):
    return len(text)


# Function to count for the number of symbols.
def numberOfSymbols(message):
    count = 0
    all_punctuation = string.punctuation
    for letter in message:
        if letter in all_punctuation:
            count += 1
    return count


# Function to write to a CSV file.
def writingToCSV(file_name, lines):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)


def main():
    # List of possible links and spam words.
    list_links = ["http", "www", "::", "//", ":", ".com", ".uk", ".biz", "https", ".net"]
    list_spamwords = ["spam", "click", "call", "text", "free", "press", "award", "prize", "txt", "claim", "guaranteed",
                      "urgent", "private", "win", "won", "ansr", "rcv", "svc", "go", "stop", "msg", "join", "reply",
                      "unsubscribe", "charge", "entitled", "send", "congrats", "collect", "activate", "congratulations",
                      "unsub", "xclusive", "chat", "offer", "expire", "get", "sms", "forwarded", "alert", "vary",
                      "charges", "subscribe", "unclaimed", "unsub", "visit", "opt out", "new", "trial", "redeemed",
                      "redeem", "content", "download", "chat", "winner"]

    # Creating a features list with the first row being the labels for features.csv file.
    features_list = [["doesHaveLinks", "doesHaveSpammyWords", "lengthOfText", "numberOfSymbols", "classLabel"]]

    # Reading data.
    with open('spam.csv', 'r', encoding="ISO-8859-1") as in_file:
        csv_reader = csv.reader(in_file, delimiter=',')

        # Making first row as headers.
        header_row = next(csv_reader)

        # Recording each row and creating object.
        for row in csv_reader:
            text = row[1].lower()
            class_label = row[0].lower()

            features_row = list()
            links = doesHaveLinks(list_links, text)
            spam_words = doesHaveSpammyWords(list_spamwords, text)
            symbols = numberOfSymbols(text)
            length = lengthOfText(text)

            message = Message(class_label, text, spam_words, length, symbols, links)
            features_row.append(links)
            features_row.append(spam_words)
            features_row.append(length)
            features_row.append(symbols)
            features_row.append(class_label)
            features_list.append(features_row)
    # Creating .arff file for WEKA.
    writingToCSV('features.arff', features_list)

    # Creating .csv file as well.
    writingToCSV('features.csv', features_list)


main()
