from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
import time, re


def filler_word_analysis(sentence):

    console = Console()

    with Progress(

        SpinnerColumn(),
        TextColumn("[progess.description]{task.description}"),
        console= console,
        transient= True
    
    ) as progbar:

        progbar.add_task(description="Analyzing filler words in sentence....", total=None)

        filler_words = {

            'um', 'uh', 'er', 'ah', 'like', 'basically', 'literally', 'actually', 'well',
            'so', 'right', 'okay', 'just', 'stuff', 'things'
        } 

        filler_phrases = {

            'you know', 'sort of', 'kind of', 'i mean', 'you see'
        }

        time.sleep(5)

        cleaned_sentence = sentence.lower().strip()

        words = [word for word in re.split(r'[,\s]+', cleaned_sentence) if word]
        total_words = len(words)

        filler_word_count = {}
        total_filler_words = {}

        detect_filler_phrases = ' '.join(words)

        for phrase in filler_phrases:

            count = sum(1 for i in range(len(words) - 1) if ' '.join(words[i:i + 2]).lower() == phrase)

            if count > 0:
                filler_word_count[phrase] = count
                total_filler_words += count

        for word in filler_words:

            count = sum(1 for w in words if w.lower() == word)

            if count > 0:
                filler_word_count[word] = count
                total_filler_words += count

        filler_words_percentage = (total_filler_words / total_words * 100) if total_words > 0 else 0

        return {

            'Total Words': total_words,
            'Total Filler Words': total_filler_words,
            'Percentage of filler words': round(filler_words_percentage, 2),
            'Filler_words Used': dict(sorted(filler_word_count.items(), key= lambda X: x[1], reverse=True))
        }


    