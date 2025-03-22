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

        filler_words_count = {}
        total_filler_words = 0

        detect_filler_phrases = ' '.join(words)

        for phrase in filler_phrases:

            count = sum(1 for i in range(len(words) - 1) if ' '.join(words[i:i+2]).lower() == phrase)

            if count > 0:
                filler_words_count[phrase] = count
                total_filler_words += count

        for word in filler_words:

            count = sum(1 for w in words if w.lower() == word)

            if count > 0:
                filler_words_count[word] = count
                total_filler_words += count

        filler_words_percentage = (total_filler_words / total_words * 100) if total_words > 0 else 0

        return {

            'Total Words': total_words,
            'Total Filler Words': total_filler_words,
            'Percentage of filler words': round(filler_words_percentage, 2),
            'Filler Words Used': dict(sorted(filler_words_count.items(), key= lambda x: x[1], reverse=True))
        }


def display_results(result):
    console = Console()

    console.print("\n[bold green]Analysis Complete![/bold green]\n")

    console.print("[bold blue]Summary:[/bold blue]")
    console.print(f"📝 Total words: {result['Total Words']}")
    console.print(f"🔍 Total filler words: {result['Total Filler Words']}")
    console.print(f"📊 Filler words percentage: [bold]{result['Percentage of filler words']}%[/bold]")

    console.print("\n[bold blue]Filler Words Breakdown:[/bold blue]")
    if result['Filler Words Used']:
        for word, count in result['Filler Words Used'].items():
            console.print(f"  • '{word}': {count} time(s)")
    else:
        console.print("  No filler words found!")

if __name__ == "__main__":
    sentence = """Well, like, you know, I mean, basically, the thing is that, um, actually, the cat sort of jumped over, uh, the fence and, well, kind of ran into, you see, the neighbor's yard where, essentially, it started to, um, chase after, like, this really small and, you know, kind of energetic squirrel that was, basically, just minding its own business while, uh, gathering nuts and, well, other things that, like, squirrels typically, um, gather during this, you know, time of year when, basically, the weather starts to, uh, get colder and, well, animals need to, like, prepare for winter by, um, storing food and, you know, making their nests more, basically, comfortable and, uh, warm which, well, is really important for, like, their survival during the, um, harsh winter months when, you know, food becomes, basically, scarce and, uh, temperatures drop to, well, really low levels that, like, make it difficult for, um, small animals to, you know, maintain their body heat and, basically, stay alive through the, uh, coldest parts of, well, winter which, like, can last for, um, several months in, you know, certain regions where, basically, the climate is, uh, more severe and, well, winter storms can, like, dump feet of, um, snow on the, you know, ground making it, basically, impossible for, uh, animals to, well, find food unless they've, like, prepared properly by, um, storing enough, you know, nuts and seeds to, basically, last them through the, uh, winter months until, well, spring arrives and, like, brings with it, um, warmer temperatures and, you know, new growth that, basically, provides fresh food sources for, uh, all the animals that, well, managed to, like, survive through the, um, difficult winter by, you know, either hibernating or, basically, relying on their, uh, stored food supplies which, well, they gathered during, like, the warmer months when, um, food was plentiful and, you know, easier to find because, basically, plants were growing and, uh, producing seeds and, well, fruits that, like, animals could, um, eat or store for, you know, later use during the, basically, lean times of, uh, winter when, well, survival becomes, like, much more challenging for, um, all creatures in the, you know, natural world."""
    
    console = Console()
    console.print("\n[bold yellow]Starting Text Analysis...[/bold yellow]")
    
    result = filler_word_analysis(sentence)
    display_results(result)