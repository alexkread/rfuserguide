
some_value = f"""
    Note\n
    Some single line text here
"""
three_digit_heading_text = "4.1.1   Test & something 4.1.1 else      here   4.1.1   Maybe?"

single_text_rest_note_line_break_after = rf"""
    Note\n 
    Some single line text here
"""
single_text_rest_note_line_break_after_expected = """!!! note

Some single line text here"""
two_sentence_text_rest_note_line_break_after = """
Note

Some single line text here. But another text line here.

"""
single_paragraph_text_rest_note_line_break_after = """
Note

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

"""
single_text_rest_note_line_breaks_beforeafter = """

Note

Some single line text here  

"""
two_sentence_text_rest_note_line_breaks_beforeafter = """

Note

Some single line text here. But another text line here.

"""
single_paragraph_text_rest_note_line_breaks_beforeafter = """

Note

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

"""
single_text_rest_note_dual_line_breaks_beforeafter = """


Note

Some single line text here  


"""
two_sentence_text_rest_note_dual_line_breaks_beforeafter = """


Note

Some single line text here. But another text line here.


"""
single_paragraph_text_rest_note_dual_line_breaks_beforeafter = """


Note

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.


"""