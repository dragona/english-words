"""
Permission is hereby granted, free of charge, 
to any person obtaining a copy of this software 
and associated documentation files (the "Software"), 
to deal in the Software without restriction, 
including without limitation the rights to use, 
copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit 
persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice 
shall be included in all copies or substantial portions 
of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF 
ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED 
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH 
THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


"""

import os
import glob
from pathlib import Path

"""
This script gets the words from the datasets listed below and generates a dictionary.txt file that contains all the 
unique words from the dictionary.
"""


def process_sim() -> set():
    """
    Requirements:
        Download the original dataset from http://www.cs.cornell.edu/home/llee/data/simdata.tar.gz
        Unzip the files test1.gz, test2.gz, test3.gz, test4.gz, test5.gz, and train.gz and place
        the corresponding data in the dataset folder

    The code:
        The script loads all files from the dataset folder,
        Gets the files text content, per line, then retrieves each word to build a set of unique words.
    :return a collection of unique words
    """
    # reading all the files
    words_ = set()
    for file in glob.glob("./dataset/*"):
        f_handle = open(file, 'rb')
        counter = 0
        for word in f_handle.read().decode(errors='ignore').encode('utf-8').split():
            if word.isalpha():
                words_.add(word.lower())
            counter += 1
        print('File name: {} - Unique words cumulated: {} - String in the file: {} '.format(file, len(words_), counter))

    return words_


def process_scol() -> set():
    """
    Read all the files all the scowl-2019.10.06 which was the un-compressed dataset from
    http://downloads.sourceforge.net/wordlist/scowl-2019.10.06.tar.gz
    http://wordlist.aspell.net/

    Get all unique words from all files in the whole package.

    :return a collection of the words

    """
    all_ = list(Path("./scowl-2019.10.06/").rglob('*'))  # including files and directories
    files = [_ for _ in all_ if os.path.isfile(_)]
    counter_file = 0
    words = set()
    for filename_path in list(files):
        f_handle = open(filename_path, 'rb')
        counter_file += 1
        counter = 0
        for word in f_handle.read().decode(errors='ignore').encode('utf-8').split():
            if word.isalpha():
                words.add(word.lower())
            counter += 1
        print(
            '{0:>3} / {1:3} #  {2:<70} # Unique words cumulated: {3:<8} - String in the file: {4}'.format(counter_file,
                                                                                                          len(files),
                                                                                                          str(
                                                                                                              filename_path),
                                                                                                          len(words),
                                                                                                          counter))
    return words


def save(words: []) -> None:
    f = open("dictionary.txt", "a")
    for _ in words:
        # print(type(_), _)
        # handle byte case instead of string
        if isinstance(_, bytes):
            _ = _.decode()
        f.write(_ + "\n")
    f.close()
    print("Completed writing")


if __name__ == '__main__':
    words = process_sim()
    words = list(words.union(process_scol()))
    words.sort(reverse=False)
    save(words)
