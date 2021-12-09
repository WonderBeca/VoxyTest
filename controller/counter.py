def parse_counters(text: str) -> dict:
    """
        This funcion count how many words, sentences, characters and paragraphs
        a text have.

    Args:
        text (str): A user text input

    Returns:
        dict: A dict containing the number of words, sentences, characters and paragraphs has the input text
    """    
    data = {
        'characters': len(text),
        'words': len(text.split(' ')),
        'paragraphs': len(text.split('\n')),
        'sentences': sentence_counter(text)
    }

    return data 

def sentence_counter(text: str) -> int:
    """
        This function count how many sentences a text have

    Args:
        text (str): A user text input

    Returns:
        int: A integer containing the number of sentences has the input text
    """    
    sentence_count = 0
    seen_end = False
    sentence_end = {'?', '!', '.', '\n'}
    for c in text:
        if c in sentence_end:
            # For the sentences that have something like: AMAZING!!!!
            if not seen_end:
                seen_end = True
                sentence_count += 1
            continue
        seen_end = False

    return sentence_count