# coding:utf8

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')

        fout.write("<html><body><table>")

        for data in self.datas:
            print(data['url'])
            print(data['title'])
            print(data['summary'])
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'].encode('GBK', 'ignore'))
            fout.write("<td>%s</td>" % data['title'].encode('GBK', 'ignore'))
            fout.write("<td>%s</td>" % data['summary'].encode('GBK', 'ignore'))
            fout.write("</tr>")

        fout.write("</table></body></html>")

        fout.close()