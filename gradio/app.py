import gradio as gr
import os
import requests

def id_check(frame):
    url = "http://127.0.0.1:8082/api/id_check"
    files = {'image': open(frame, 'rb')}
    r = requests.post(url=url, files=files)

    html = None
    images = None
    mrz = None

    table_value = ""

    if r.json().get('MRZ') is not None:
        mrz = r.json().get('MRZ')

    for key, value in r.json().items():
        if key == 'Status' or key == 'Images' or key == 'MRZ' or key == 'Position':
            continue

        mrz_value = ''
        if mrz is not None and mrz.get(key) is not None:
            mrz_value = mrz[key]
            del mrz[key]

        row_value = ("<tr>"
                        "<td>{key}</td>"
                        "<td>{value}</td>"
                        "<td>{mrz_value}</td>"
                    "</tr>".format(key=key, value=value, mrz_value=mrz_value))
        table_value = table_value + row_value


    if mrz is not None:
        for key, value in mrz.items():
            if key == 'MRZ':
                value = value.replace('<', '&lt;')
                value = value.replace(',', '<p>')

            row_value = ("<tr>"
                            "<td>{key}</td>"
                            "<td>{value}</td>"
                            "<td>{mrz_value}</td>"
                        "</tr>".format(key=key, value='', mrz_value=value))
            table_value = table_value + row_value
            

    html = ("<table>"
                "<tr>"
                    "<th style=""width:20%"">Field</th>"
                    "<th style=""width:40%"">Value</th>"
                    "<th style=""width:40%"">MRZ</th>"
                "</tr>"
                "{table_value}"
                "</table>".format(table_value=table_value))
    
    table_value = ""
    for key, value in r.json().items():
        if key == 'Images':
            for image_key, image_value in value.items():
                row_value = ("<tr>"
                                "<td>{key}</td>"
                                "<td><img src=""data:image/png;base64,{base64_image} width = '200'  height= '100' /></td>"
                            "</tr>".format(key=image_key, base64_image=image_value))
                table_value = table_value + row_value

    images = ("<table>"
                "<tr>"
                    "<th>Field</th>"
                    "<th>Image</th>"
                "</tr>"
                "{table_value}"
                "</table>".format(table_value=table_value))
    
    return [html, images]

def bank_credit_check(frame):
    url = 'http://127.0.0.1:8082/api/bank_credit_check'
    files = {'image': open(frame, 'rb')}
    r = requests.post(url=url, files=files)

    html = None
    table_value = ""

    for key, value in r.json().items():
        if key == 'Status' or key == 'Images':
            continue

        row_value = ("<tr>"
                        "<td>{key}</td>"
                        "<td>{value}</td>"
                    "</tr>".format(key=key, value=value))
        table_value = table_value + row_value

    html = ("<table>"
                "<tr>"
                    "<th style=""width:20%"">Field</th>"
                    "<th style=""width:40%"">Value</th>"
                "</tr>"
                "{table_value}"
                "</table>".format(table_value=table_value))
        
    return html

def mrz_barcode_check(frame):
    url = 'http://127.0.0.1:8082/api/mrz_barcode_check'
    files = {'image': open(frame, 'rb')}
    r = requests.post(url=url, files=files)

    html = None
    mrz = None

    table_value = ""

    if r.json().get('MRZ') is not None:
        mrz = r.json().get('MRZ')

    # Iterate through the MRZ data and print each key and item
    for key, value in mrz.items():
        if key == 'MRZ Code':
            value = value.replace('<', '&lt;')
            value = value.replace(',', '<p>')
        row_value = ("<tr>"
                "<td>{key}</td>"
                "<td>{value}</td>"
            "</tr>".format(key=key, value=value))
        table_value = table_value + row_value

    html = ("<table>"
                "<tr>"
                    "<th style=""width:20%"">Field</th>"
                    "<th style=""width:40%"">Value</th>"
                "</tr>"
                "{table_value}"
                "</table>".format(table_value=table_value))
        
    return html

# APP Interface
with gr.Blocks() as MiniAIdemo:
    gr.Markdown(
        """
        <a href="https://miniai.live" style="display: flex; align-items: center;">
            <img src="https://miniai.live/wp-content/uploads/2024/02/logo_name-1-768x426-1.png" style="width: 18%; margin-right: 15px;"/>
            <div>
                <p style="font-size: 50px; font-weight: bold; margin-right: 20px;">IDSDK Web Online Demo</p>
            </div>
        </a>

        <br/>
        <ul>
            <li style="font-size: 18px;">Visit and learn more about our Service : <a href="https://miniai.live" target="_blank" style="font-size: 18px;">https://www.miniai.live</a></li>
            <li style="font-size: 18px;">Check our SDK for cross-platform from Github : <a href="https://github.com/MiniAiLive" target="_blank" style="font-size: 18px;">https://github.com/MiniAiLive</a></li>
            <li style="font-size: 18px;">Quick view our Youtube Demo Video : <a href="https://www.youtube.com/@miniailive" target="_blank" style="font-size: 18px;">MiniAiLive Youtube Channel</a></li>
            <li style="font-size: 18px;">Demo with Android device from Google Play : <a href="https://play.google.com/store/apps/dev?id=5831076207730531667" target="_blank" style="font-size: 18px;">MiniAiLive Google Play</a></li>
        </ul>
        <br/>
        """
    )
    with gr.Tabs():
        with gr.TabItem("ID Card Recognition"):
            with gr.Row():
                with gr.Column(scale=3):
                    im_id_input = gr.Image(type='filepath', height=300)
                    gr.Examples(
                        [
                            os.path.join(os.path.dirname(__file__), "images/id/demo1.jpg"),
                            os.path.join(os.path.dirname(__file__), "images/id/demo2.png"),
                            os.path.join(os.path.dirname(__file__), "images/id/demo3.png"),
                        ],
                        inputs=im_id_input
                    )
                    btn_f_id = gr.Button("Analysis Document", variant='primary')
                with gr.Column(scale=5):
                    txt_id_output = gr.HTML()
                with gr.Column(scale=2):
                    im_id_output = gr.HTML()
            btn_f_id.click(id_check, inputs=im_id_input, outputs=[txt_id_output, im_id_output])
        with gr.TabItem("Bank & Credit Card Recognition"):
            with gr.Row():
                with gr.Column(scale=3):
                    im_card_input = gr.Image(type='filepath', height=300)
                    gr.Examples(
                        [
                            os.path.join(os.path.dirname(__file__), "images/band_credit_card/demo1.jpg"),
                            os.path.join(os.path.dirname(__file__), "images/band_credit_card/demo2.png"),
                            os.path.join(os.path.dirname(__file__), "images/band_credit_card/demo3.png"), 
                        ],
                        inputs=im_card_input
                    )
                    btn_f_card = gr.Button("Analysis Document", variant='primary')
                with gr.Column(scale=5):
                    txt_card_output = gr.HTML()
            btn_f_card.click(bank_credit_check, inputs=im_card_input, outputs=txt_card_output)
        with gr.TabItem("MRZ & Barcode Recognition"):
            with gr.Row():
                with gr.Column(scale=3):
                    im_mrz_input = gr.Image(type='filepath', height=300)
                    gr.Examples(
                        [
                            os.path.join(os.path.dirname(__file__), "images/mrz_barcode/demo1.png"),
                            os.path.join(os.path.dirname(__file__), "images/mrz_barcode/demo2.png"), 
                        ],
                        inputs=im_mrz_input
                    )
                    btn_f_mrz = gr.Button("Analysis Document", variant='primary')
                with gr.Column(scale=5):
                    txt_mrz_output = gr.HTML()
            btn_f_mrz.click(mrz_barcode_check, inputs=im_mrz_input, outputs=txt_mrz_output)

if __name__ == "__main__":
    MiniAIdemo.launch(server_port=8083, server_name="0.0.0.0")