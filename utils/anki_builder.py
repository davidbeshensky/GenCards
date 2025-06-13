import genanki
import uuid

def create_deck(flashcards, output_path='output/output_flashcards.apkg'):
    model = genanki.Model(
        model_id=uuid.uuid4().int >> 96,
        name='YT Flashcards',
        fields=[{'name': 'Question'}, {'name': 'Answer'}, {'name': 'Image'}],
        templates=[{
            'name': 'Card Template',
            'qfmt': '{{Image}}<br><br>{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        }]
    )

    deck = genanki.Deck(uuid.uuid4().int >> 96, 'YouTube Learning Deck')

    for card in flashcards:
        note = genanki.Note(
            model=model,
            fields=[card['q'], card['a'], f'<img src="{card["img"]}">']
        )
        deck.add_note(note)

    package = genanki.Package(deck)
    package.media_files = [card['img'] for card in flashcards]
    package.write_to_file(output_path)
