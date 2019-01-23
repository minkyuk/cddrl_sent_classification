# cddrl_sent_classification
Challenge of classifying legal documents, such as ones from Federal Communication Commissions, using various state-of-art sentence vectorization and unsupervised classification method. 

The current code includes the FCC API key that was used to scrap the documents from EFCS data base.
A new regulations.gov API Key can be requested and registered with a working institutional e-mail as the currently registered e-mail has expired.

params.py contains a basic structure to simply add/delete attributes to a parameter class. In the current code, I decided to put all the directory informations and dynamically-obtained json files to have instant access to it while the code is running so that one does not have to make a file-read whenever we need access to the documents.

The current code contains a specific data collecting function from EFCS server using downloadplan.

When scrapping files from FCC, I save the documents from each bucket (which may vary in number) into a folder 'output_docs'. This folder is created if it doesn't exist. Then, it saves the downloadplan data in a txt file in it.
Each document/bucket has an id corresponding to it, and for all documents scrapped, the ids are logged dynamically in a txt file 'filing.txt'.
Then, optionally, at each time of execution of read on each document, the documents are converted into json and are saved to params AND 'all_json_text.txt', or any chosen name in the parameter, in the global project folder.
This makes a cushion for reading json file directly from saved json instead of reading each bucket and converting them into json in case of a failed save in dynamic parameter class.

On each scrapped documents, there are three pre-processing types: raw text, slightly raw text with most basic stop words taken out, and text in which all known stop words are taken out.
One can choose which list of stop words to use; in this current code, I used the one from NLTK library.

Then, one can easily use any kind of vectorization function to vectorize the text, whether if it's raw or pre-processed before putting it through unsupervised classification.

Those vectors can get fed into any algorithm to create a correlational matrix. 
The current approach relies on Simple, but Hard to Beat Baseline paper and GloVe 300 dimensional vector for each word.

https://openreview.net/pdf?id=SyK00v5xx

https://github.com/stanfordnlp/GloVe

The value of alpha(a) can be adjusted from parameter class, which represents the frequency of the word. More details can be found in the paper.
The current code uses tf-idf correlational matrix as a baseline to beat. 

There are other vectorizations method such as sent2vec, fasttext, etc. that can be swapped out and be compared with.

The final unsupervised visualization part is t-SNE(https://lvdmaaten.github.io/tsne/) with varying number of dimension of choice in the parameter of the function.
This method uses pairwise distance instead of Euclidian distance to cluster dimension-reduced documents.

Nearest neighbor search was done by K-d tree, which is not the only method to do find the nearest neighbors.

