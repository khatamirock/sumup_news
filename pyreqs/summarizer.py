import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import random


sent = ''


def cleanText(text):

    text = re.sub(r'\n|\r', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.strip()
    sent = text.split('।')
    sent2 = text.split('.')

    if len(sent) < len(sent2):
        sent = sent2[:-1]

    return sent


def tokner(str):
    return str.split()


def getSimmat(sent):
    vectorizer = TfidfVectorizer(tokenizer=tokner)
    vectors = vectorizer.fit_transform(sent)
    dt_matrix = vectors.toarray()

    similarity_matrix = np.matmul(dt_matrix, dt_matrix.T)
    return similarity_matrix


def run_page_rank(similarity_matrix):

    # constants
    damping = 0.85  # damping coefficient, usually is .85
    min_diff = 1e-5  # convergence threshold
    steps = 100  # iteration steps

    pr_vector = np.array([1] * len(similarity_matrix))

    # Iteration
    previous_pr = 0
    for epoch in range(steps):
        pr_vector = (1 - damping) + damping * \
            np.matmul(similarity_matrix, pr_vector)
        # print(pr_vector)
        if abs(previous_pr - sum(pr_vector)) < min_diff:
            break
        else:
            previous_pr = sum(pr_vector)

    return pr_vector


def get_top_sentences(pr_vector, sentences, number):

    top_sentences = ''

    if pr_vector is not None:

        sorted_pr = np.argsort(pr_vector)
        # print(sorted_pr)
        sorted_pr = list(sorted_pr)
        # it means from big to small... the upper thing was for small to big >>  ascending...............
        sorted_pr.reverse()
        # print(sorted_pr)
        sorted_pr = sorted_pr[:10]
        # print(sorted_pr)
        index = 0
        sorted_pr.sort()
        # print(sorted_pr)
        left = number
        for epoch in range(number//2+2):
            sent = sentences[sorted_pr[index]]
            # sent = normalize_whitespace(sent)
            top_sentences += sent+' । '
            if index % 2 == 0:
                top_sentences += '\n'
            index += 1
#       print(top_sentences)
        sorted_pr = sorted_pr[left+1:]
        random.shuffle(sorted_pr)

        for epoch in range(left):
            sent = sentences[sorted_pr[epoch]]
            # sent = normalize_whitespace(sent)
            top_sentences += sent+' । '
            if index % 2 == 0:
                top_sentences += '\n'
            index += 1
    return top_sentences
