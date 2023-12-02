import pdfkit
import pandas as pd
import base64
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe

st.set_page_config(layout="centered", page_icon="🎓", page_title="Tender Generator")
st.title(" Tender Form")

st.write(
    "This app shows you how to generate tender form"
)

col1, col2,col3 = st.columns(3)



#right.image("template.png", width=300)

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")


col1.write("ပထမအကြိမ်ဈေးနှုန်းများ")
form = col1.form("template_form")
student = form.text_input("Price")
count = form.text_input("Count")
first = form.text_input("First Price")
second = form.text_input("Second Price")
third = form.text_input("Third Price")
tender_price = form.text_input("Tender Price")




col2.write("ဒုတိယအကြိမ်ဈေးနှုန်းများ")
form = col2.form("Information")
price2 = form.text_input("Price")
count2 = form.text_input("Count")
first2 = form.text_input("First Price")
second2 = form.text_input("Second Price")
third2 = form.text_input("Third Price")
tender_price2 = form.text_input("Tender Price")

#submit = form.form_submit_button("Generate PDF")



col3.write("တတိယအကြိမ်ဈေးနှုန်းများ")
form = col3.form("Third Information")
price3 = form.text_input("Price")
count3 = form.text_input("Count")
first3 = form.text_input("First Price")
second3 = form.text_input("Second Price")
third3 = form.text_input("Third Price")
tender_price3 = form.text_input("Tender Price")

submit = form.form_submit_button("Generate PDF")

df = pd.DataFrame(columns=['ကြမ်းခင်းဈေး', 'အကြိမ်ရေ','ပထမအကြိမ်','ဒုတိယအကြိမ်','တတိယအကြိမ်','လေလံဈေး'])

if submit:
    st.write(student,first)
    new_data = {"ကြမ်းခင်းဈေး":student,"အကြိမ်ရေ":count,"ပထမအကြိမ်":first,"ဒုတိယအကြိမ်":second,"တတိယအကြိမ်":third,"လေလံဈေး":tender_price,"ကြမ်းခင်းဈေး":price2,"အကြိမ်ရေ":count2}
    df1 = df.append(new_data,ignore_index=True)
    st.write(df1)

    st.checkbox("User container width",value=False,key="use_container_width")

    st.dataframe(df,use_container_width=st.session_state.use_container_width)

    def filedownload(df1):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="record.csv">Download CSV File</a>'
        return href
    st.markdown(filedownload(df),unsafe_allow_html=True)

if submit:
    html = template.render(
        student=student,
        first = first,
        second=second,
        third=third,
        tender_price=tender_price,

        date=date.today().strftime("%B %d, %Y"),
    )



    pdf = pdfkit.from_string(html, False)
    st.balloons()

    col3.success("🎉 Your diploma was generated!")
    # st.write(html, unsafe_allow_html=True)
    # st.write("")
    col3.download_button(
        "⬇️ Download PDF",
        data=pdf,
        file_name="diploma.pdf",
        mime="application/octet-stream",
        )
