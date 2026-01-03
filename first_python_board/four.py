from flask import Flask, render_template, request, redirect, url_for


class SimpleBoard:
    def __init__(self, name):
        self.app = Flask(name)
        self.post = [
            {"id": 1, "title": "첫 번째 글", "content": "첫 번째 글 내용"},
        ]


        @self.app.route('/')
        def index():
            return render_template('index.html', post=self.post)

        @self.app.route('/write', methods=['POST'])
        def write():
            title = request.form.get('title')
            content = request.form.get('content')

            if title and content:
                new_id = len(self.post) + 1
                self.post.append({
                    "id": new_id,
                    "title": title,
                    "content": content
                })

            return redirect(url_for('index'))

    def run(self):
        self.app.run(debug=True)


if __name__ == "__main__":
    board = SimpleBoard(__name__)
    board.run()