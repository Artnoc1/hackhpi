from typing import List, Tuple

from conll_reader import WordInfo


def generate_html(sentences: List[List[WordInfo]]) -> str:
    color=""
    result = """<!DOCTYPE html>
        <html>
        <head>
        <style>
        div[class^=word].word0 {
            color: grey;
        }
        div[class^="word"]{
            color: black;
            position: relative;
            display: inline-block
        }
        div[class^="word"] .tooltiptext {
            visibility: hidden;
            width: 120px;
            background-color: black;
            color: #fff;
            text-align: center;
            border-radius: 6px;
            padding: 5px 0;
            position: absolute;
            z-index: 1;
            bottom: 100%;
            left: 50%;
            margin-left: -60px;

            /* Fade in tooltip - takes 0.5 second to go from 0% to 100% opac: */
            opacity: 0;
            transition: opacity 0.5s;
        }

        div[class^=word]:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
        </style>
        </head>
        <body>
        """
    for sentence in sentences:
        for word in sentence:
             is_root= word.is_root_subject or word.is_root_verb
             if is_root:
                 color = "red"
             result += "" \
                      "<div class=\"word{0}\">{1} \
<<<<<<< HEAD
                       <span class=\"tooltiptext\" style=\"{2}\">{3}</span> \
                       </div>".format(str(word.importance), word.word, color, word.word_class)
             result += " "

        
=======
                       <span class=\"tooltiptext\">{2}</span> \
                       </div>".format(str(word.importance), word.word, str(word.nesting_level) + word.word_class)
            result += " "
>>>>>>> eaf1e167b1ef62b38b4f4a53fd73f7327d2c2bef

    result += """
        </body>
        </html>
        """

    return result
