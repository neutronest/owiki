#-*- coding:utf-8 -*-
import markdown
import sys
from flask import Flask
from flask import render_template
from flask import Markup
from flask import request
import logging

import wiki_config
import utils

app = Flask(__name__)

@app.route("/index", methods=['GET'])
def index():
    """
    """

    path = request.args.get("path")
    print path
    if path == None:
        md_content = "Welcome to owiki!"
    else:

        # get wiki content
        # path format: category:wiki_name
        path_arr = path.split(":")
        category = path_arr[0]
        wiki_name = path_arr[1]

        wiki_url = wiki_config.wiki_root + category + "/" + wiki_name+".md"
        logging.info(wiki_url)
        md_str = []
        with open(wiki_url, "r") as file_ob:
            for line in file_ob:
                logging.info(line)
                md_str.append(line)
        file_ob.close()
        md_str = '\n'.join(md_str)
        logging.info(md_str)
        md_content = Markup(markdown.markdown(md_str.decode("utf-8")))

    # get category
    category_dict = {}
    category_dict = utils.folder_travel(wiki_config.wiki_root)



    return render_template('index.html', md_content=md_content,
                           category_dict=category_dict)

if __name__ == "__main__":
    # get argv
    print "owiki yi-go-you~~~~"
    command = sys.argv[1]
    if command == "run":
        app.debug = True
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.INFO)
        app.run()
    elif command == "new_post":
        assert(len(sys.argv) > 2)
        filepath = sys.argv[2]
        with open(filepath, "w") as file_ob:
            print "make new post in ", filepath
        file_ob.close()
    else:
        print "not supported command"
