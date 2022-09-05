#!/usr/bin/env python

import csv
from collections import Counter


class Recipient:

    def __init__(self, recipient="", subject=""):
        self.recipient = recipient
        self.subject = subject



if __name__ == '__main__':

    with open('sample.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        rec_list = list()
        line_count = 0
        for row in csv_reader:
            if line_count != 0 and line_count != 1:
                # line 0 and line 1 are headers
                rec_list.append(Recipient(
                    recipient=row[0],
                    subject=row[1]
                    )
                )
            line_count = line_count + 1
            #print("line_count: ", line_count)

        # list element must be sorted by subject
        rec_list.sort(key=lambda k: k.subject)
        
        # User Counter to easily count element by subject and by recipient
        counted_mail = Counter((rec.subject, rec.recipient) for rec in rec_list)

        # Get number of élement in Counter
        print("Number of email sent: ", counted_mail.total())

        # Create a usable output
        output = [({
            'Subject': s,
            'Recipient': r
        }, k) \
        for (s, r), k in counted_mail.items()]

        # Print result into a table
        print("| {:<125} | {:<50} | {:<6} |".format("Subject", "Recipient", "Total"))
        print("|{}|{}|{}|".format(127*'-', 52*'-', 8*'-'))
        for elt in output: 
            print("| {:<125} | {:<50} | {:<6} |".format(elt[0]['Subject'], elt[0]['Recipient'], elt[1]))

        #c = Counter(getattr(email, 'recipient') for email in rec_list)
        #print(c)







