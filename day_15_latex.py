import streamlit as st

st.header("st.latex")

example_latex_string = """
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)

''')

"""

st.code(example_latex_string)

st.latex(
    r"""
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)

"""
)

st.markdown(
    "Latex cheatsheet [here](http://tug.ctan.org/info/latex-refsheet/LaTeX_RefSheet.pdf)"
)
