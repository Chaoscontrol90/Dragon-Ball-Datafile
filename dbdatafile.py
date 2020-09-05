#object-oriented programming
class Saiyan:
    def __init__(self, name, techniques, transformations):
        self.name = name
        self.techniques = techniques
        self.transformations = transformations

    def intro(self):
        print(f"{self.name} is a Saiyan, a warrior race from Planet Vegeta.")
#inheritance

class HalfSaiyan(Saiyan):
    def __init__(self, name, techniques, transformations):
        super().__init__(name, techniques, transformations)
        self.name = name
        self.techniques = techniques
        self.transformations = transformations

    def intro(self):
        print(f"{self.name} is a half-Saiyan, an offspring of a Saiyan and a human.")


class Universe6Saiyan(Saiyan):
    def __init__(self, name, techniques, transformations):
        super().__init__(name, techniques, transformations)
        self.name = name
        self.techniques = techniques
        self.transformations = transformations

    def intro(self):
        #super(Universe6Saiyan, self).intro()
        print(f"{self.name} is a Saiyan, a warrior race from Universe 6's Planet Sadala.")


class Fusion(Saiyan):
    def __init__(self, name, techniques, transformations):
        super().__init__(name, techniques, transformations)
        self.name = name
        self.techniques = techniques
        self.transformations = transformations

    def intro(self):
        #super(Fusion, self).intro()
        print(f"{self.name} is a fusion with the Potara earrings or the fusion dance.")


class Human:

    def __init__(self, name, techniques):
        self.name = name
        self.techniques = techniques

    def intro(self):
        print(f"{self.name} is a human that practices martial arts. He defends the Earth from great threats.")


class Android(Human):

    def __init__(self, name, techniques):
        super().__init__(name, techniques)
        self.name = name
        self.techniques = techniques

    def intro(self):
        print(f"{self.name} is an Android created by Dr.Gero. \nThey have superhuman strength and infinite stamina.")






class God:
    def __init__(self, name, status, techniques):
        self.name = name
        self.status = status
        self.techniques = techniques

    def intro(self):
        print(f"Here's the info for {self.name}.")


class GodofDestruction(God):
    def __init__(self, name, status, techniques):
        super().__init__(name, status, techniques)
        self.name = name
        self.status = status
        self.techniques = techniques

    def intro(self):
        print(f"{self.name} is a God of Destruction, responsible of maintaining balance and order in their universe.")


class Angel(God):
    def __init__(self, name, status, techniques):
        super().__init__(name, status, techniques)
        self.name = name
        self.status = status
        self.techniques = techniques

    def intro(self):
        print(f"{self.name} is an Angel, responsible for keeping the God of Destruction in line.")


class SupremeKai(God):
    def __init__(self, name, status, techniques):
        super().__init__(name, status, techniques)
        self.name = name
        self.status = status
        self.techniques = techniques

    def intro(self):
        print(f"{self.name} is an Supreme Kai. \nAlong with the God of Destruction, they keep the peace in their universe.")


class Namekian:

    def __init__(self, name, techniques):
        self.name = name
        self.techniques = techniques

    def intro(self):
        print(f"{self.name} is a Namekian, a race of people who are from the planet Namek. \nThey created a miniature version of the Dragon Balls.")


class Villain:
    def __init__(self, name, techniques, transformations):
        self.name = name
        self.techniques = techniques
        self.transformations = transformations

    def intro(self):
        print(f"{self.name} is a threat to the Universe. \nThe Z Fighters often have to work together to stop them. ")


class Fighter:

    def __init__(self, name, techniques):
        self.name = name
        self.techniques = techniques

    def intro(self):
        print(f"{self.name} is a powerful martial artist. The Saiyans are challenged by their unique abilities.")


Goku = Saiyan('Goku', ['Kamehameha', 'Kaioken'], ['SSJ', 'SSJ2', 'SSJ3', 'SSGod', 'SSBlue', 'Ultra Instinct:Omen','Mastered Ultra Instinct'])
Vegeta = Saiyan('Vegeta', ['Big Bang Attack','Galick Gun', 'Final Flash'], ['SSJ', 'SSJ2', 'SSGod', 'SSBlue', 'SSBlue Evolution'])
Broly = Saiyan('Broly', ['Eraser Cannon', 'Gigantic Catastrophe'], ['Great Ape Controlled', 'SSJ', 'LSSJ'])

Gohan = HalfSaiyan('Gohan', ['Kamehameha', 'Masenko'], ['SSJ', 'SSJ2', 'Mystic Form'])
Trunks = HalfSaiyan('Trunks', ['Burning Attack', 'Galick Gun', 'Final Flash'], ['SSJ', 'SSJ2', 'SS Rage'])
Goten = HalfSaiyan('Goten', 'Kamehameha', 'SSJ')

Cabba = Universe6Saiyan('Cabba', ['Galick Cannon'], ['SSJ', 'SSJ2'])
Caulifla = Universe6Saiyan('Caulifla', ['Crush Cannon', 'Burst of Energy'], ['SSJ', 'SSJ2',])
Kale = Universe6Saiyan('Kale', ['Gigantic Impact', 'Blaster Meteor'], ['SSJ', 'LSSJ', 'True LSSJ(SSJ2)'])

Gogeta = Fusion('Gogeta', ['Stardust Breaker', 'Punisher Drive'], ['SSJ', 'SSJ2', 'SSGod', 'SSBlue',])
Vegetto = Fusion('Vegetto', ['Spirit Sword', 'Big Bang Kamehameha'], ['SSJ', 'SSJ2', 'SSGod', 'SSBlue',])
Kefla = Fusion('Kefla', ['Ray Blast', 'Gigantic Blast'], ['SSJ', 'SSJ2',])

Tien = Human('Tien Shinhan', ['Tri-Beam', 'Multi-Form', ])
Krillin = Human('Krillin', ['Kamehameha', 'Kienzan', ])
Yamcha = Human('Yamcha', ['Kamehameha', 'Wolf Fang Fist', ])

a17 = Android('17', ['Barrier Punch', 'Android Barrier', ])
a18 = Android('18', ['Kienzan', 'Energy Attack', ])


Piccolo = Namekian('Piccolo', ['Makankosappo', 'Hellzone Grenade', 'Light Grenade'])

Beerus = GodofDestruction('Beerus', 'God of Destruction', ['Hakai', 'Sphere of Destruction'])
Whis = Angel('Whis', 'Angel', ['Time Reverse', 'Strike of Revealation'])
Shin = SupremeKai('Shin', 'Supreme Kai', ['Invisible Eye Blast', 'Telekinesis'])

Freeza = Villain('Freeza', ['Death Beam', 'Supernova'], ['1st form', '2nd form', 'Third Form', 'True form', 'Max Power Form', 'Golden Freeza'])
Cell = Villain('Cell', ['Kamehameha', 'Death Beam'], ['Imperfect Cell', 'Semi-Perfect Cell', 'Perfect Cell', 'Super Perfect Cell'])
Buu = Villain('Majin Buu', ['Kamehameha', 'Absorption'], ['Innocent Buu', 'Evil Buu', 'Super Buu', 'Kid Buu',])
Zamasu = Villain('Zamasu', ['God Slicer', 'Heavenly Arrow'], ['Goku Black', 'Fused Zamasu'])

Hit = Fighter('Hit', ['Time Skip', 'Time Prison'],)
Jiren = Fighter('Jiren', ['Power Impact', 'Energy Punch'],)




ss_forms = {
    'Super Saiyan' : 'First Super Saiyan transformation, first seen when Goku fights Freeza. 50x multiplier.',
    'Super Saiyan 2' :'Second Super Saiyan transformation., first seen when Gohan fights cell.100x multiplie.r',
    'Super Saiyan 3' : 'Third stage of the Super Saiyan transformation, only accessible by Goku and the fusion of Trunks and Gotenks. 400x multiplier.',
    'Mystic Form' : "Gohan's own unique form beyond SS2, symbolizing his unique evolution.",
    'Super Saiyan God' : 'The legendary Super Saiyan God form, achievable by a ritual with 5 Saiyans channeling their power, or by training with an angel.',
    'Super Saiyan Blue' : 'The Super Saiyan God form, combined with the Super Saiyan form. Also called Super Saiyan God Super Saiyan(SSGSS).',
    'Super Saiyan Blue Kaioken' : 'Kaioken stacked on top of Super Saiyan Blue.',
    'Super Saiyan Blue Evolution' : 'An evolved form of Super Saiyan Blue. Exclusive to Vegeta.',
    'Ultra Instinct: Omen' : 'The Ultra Instinct form allows autonomous movement of the body.',
    'Ultra Instinct: Mastered' : 'Mastered Ultra Instinct gives more offensive power to the Omen form, and symbolized complete mastery of the Ultra Instinct form.',
    'Great Ape': 'A controlled form of the Great Ape transformation. Broly is the only Saiyan known to know hopw to access this form.',
    'Legendary Super Saiyan' : 'The legendary Super Saiyan form, differentiated with green hair and a green aura. Can hurt the user. Gives an absurd power boost. Only accessible by Kale and Broly.',
    'Super Saiyan Rage': 'A form discovered by Trunks when he became frustrated by being unable to stop Zamasu and Goku Black.',
}

freeza_forms = {
    'First Form': "Freeza's first form. He uses this form to constrain his power",
    'Second Form': "Freeza's second form. He is at his tallest and bulkiest in this form.",
    'Third Form': "Freeza's third form. His skull increases in length and his nose combines with his mouth.",
    'Final Form': "Freeza's true form. Has a more streamlined physique.",
    "100% Full Power": "Freeza's final form with an increase in size and muscle mass.",
    "Golden Freeza": "Freeza's latest and ultimate transformation, achieved after intense training. His power is comparable to a Super Saiyan Blue."
}

cell_forms = {
    'Imperfect Cell' : "Cell's first form. This is his form before he absorbs Android 17 and 18.",
    'Semi-Perfect Cell': "Cell's second form. This is his form when he absorbs either Android 17 or 18.",
    'Perfect Cell' : "Cell's perfect form, when he has absorbed both Androids 17 and 18.",
    'Super Perfect Cell': "Cell as a Super Saiyan 2 after a zenkai boost from surviving his self-destruction."
}

buu_forms = {
    'Innoocent Buu' : "The result of Kid Buu absorbing Grand Supreme Kai.",
    'Evil Buu' : "Majin Buu's evil form dispelled from his body",
    'Super Buu' : "Evil Buu's absorption of Good Buu through turning him into chocolate",
    'Kid Buu': "The original form of Majin Buu",
}

zamasu_forms = {
    'Goku Black' : "Zamasu with Goku's body.",
    'Fused Zamasu' : "Zamasu's fusion with Goku Black.",
}

techniques = {
    'Kamehameha': "The Kamehameha is formed when cupped hands are drawn to the user's side and ki is concentrated into a single point (between their cupped hands). \nThe hands are then thrust forward to shoot out a streaming, powerful beam of energy.",
    'Kaioken': "As a result of the Kaio-ken, the user's base power level, strength, speed, and senses greatly increase for an instant.",
    'Big Bang Attack': "In order to perform it, Vegeta extends his arm, opens his palm and turns his hand up at a 90 degree angle. \nHe then condenses his ki in his palm and launches a ki blast that proceeds to detonate in a massive explosion.",
    'Galick Gun': "To utilize it, Vegeta curls his fingers and places both his hands together at chest level facing the same direction (so that the palm of one hand is on the back of the other).\nThen, once enough ki is gathered, he thrusts both hands forward to fire a powerful blast of energy. \nThe result is a powerful, huge, fuchsia-colored ki beam that emanates from his hands and body. \nIt is capable of destroying large planets if enough power is put into it.",
    'Final Flash' : "The Final Flash is formed by drawing both hands back while gathering ki. \nThen, the user places the bottom of their palms together, forming a sphere of energy that emits sporadic bolts of electric yellow ki that shoot out in all directions.\nFinally, the user discharges a massive golden beam of energy with electric ki streaming around it towards his opponent.",
    'Eraser Cannon': "First, Broly charges a green light energy from around his body and gathers it into his palm to form a bright-green energy sphere. \nNext, he waves his hand forward and fires the attack at the opponent, inflicting a large amount of damage.\n In some cases, he also fires it from his chest.",
    'Gigantic Catastrophe' : "Broly fires a mouth energy wave, followed by a series of swirling energy bullets from his left hand. \nFinally, he charges up a massive energy wave and launches it at the opponent.",
    'Masenko': "The attack is performed by the user placing both hands above the head with the palms facing the target and one hand in front of the other with the fingers going in opposite directions. \nWhen the user thrusts their hands forward, they call the name and fire a beam of yellow, white, or orange energy.",
    'Burning Attack': "Future Trunks performs a series of rapid arm movement, ending with his arms crossed across the chest, before placing his palms forward with the thumbs and index fingers touching each other, forming a diamond shape. \nThen, he fires an energy sphere from his palms towards the opponent.",
    'Galick Cannon': "Galick Cannon is performed in a manner identical to the Galick Gun",
    'Crush Cannon': "Caulifla launches several of her signature red energy blasts at the opponent in rapid succession.",
    'Burst of Energy': "Caulifla places her right arm in a horizontal position to create a red ki sphere in the hand that causes the environment to change color, then points her hand at the opponent and lifts it, shooting a gigantic wave of power from red color that causes damage to whoever is nearby.",
    'Gigantic Impact': "First, Kale charges a green light energy from around her body in the form of a seismic wave. \nNext, she gathers it into her palm to form a bright-green energy sphere. \nOnce ready, Kale waves or shoots the blast forward, inflicting a critical amount of damage. \nThis can also be charged on her chest as a defensive move.",
    'Blaster Meteor': "First, the user forms an Energy Shield around his body. \nThen, he brings his hands apart to each side and releases many powerful energy blasts that home in on the target, inflicting a massive amount of damage.",
    'Stardust Breaker': "Gogeta raises his left hand above his head, generating a ball of rainbow light before either crushing it in his palm, pivoting and flinging the scattered energy at his charging opponent, \nor flinging the prismatic sphere itself to deal immense damage to the opponent, resulting in an enormous explosion.",
    'Punisher Drive': "The user slides forward then uses Rapid Movement to attack the opponent while invisible. \nIf the attack successfully lands, multiple invisible blows land on the opponent and the user appears behind them while they are stunned.",
    'Spirit Sword': "Vegito forms the Spirit Sword by channeling his energy into his hand to form a lengthy, extendable ki blade.",
    'Big Bang Kamehameha' : 'First, the user puts both of his hands in front of him, palms open and hands turned up at approximately a 90-degree angle. \nThen, he fuses together the tremendous energy of the Super Kamehameha into a Big Bang Attack that explodes into an extremely powerful stream of ki.',
    'Ray Blast' : 'To perform this technique Kefla powers up her aura to maximum capacity and releases it continuously in several laser-like beams, which are omnidirectional.',
    'Gigantic Blast' : "This technique can be performed in a variety of ways. Kale and Caulifla can combine their energy blasts to create the beam version. \nKefla usually creates multiple green or red energy spheres on top of her hands and throws them at her opponent.",
    'Tri-Beam': "This technique is performed by gathering energy, forming a vaguely diamond-shaped 'tunnel' with the hands by keeping the fingers on each hand together, overlapping the index finger on the one hand with the pinky of the other hand, and overlapping the thumbs. \nThe object being focused on gets zoomed in on and visualized inside that diamond, then the user (namely Tien) shouts 'Tri-Beam, ha' while releasing the large yellow beam from the hands. ",
    'Multi Form': "To perform it, the users powers up and splits into two, then those two split clones into four.",
    'Kienzan': "AKA Destructo Disc.\nAn energy-based attack that consists of form a powerful razor-sharp disk of 'ki' capable of slicing through nearly any opponent.",
    'Energy Attack' : "The most basic form of energy wave used by androids.",
    'Makankosappo' : "AKA Special Beam Cannon. \nThe move is performed by touching the index and middle fingers of one hand to the forehead and charging enough ki to attack. \nIts speed changes to the power level of the user performing the move. \nWhen ready, the fingers are extended forward, and two thin energy beams are unleashed from the fingers. \nOne remains straight while the other coils around the straight beam.",
    'Hellzone Grenade': "With efficient ki control, the multiple energy spheres are suspended in the air, completely surrounding them. \nFinally, Piccolo commands the energy spheres, which change from a yellow to purple color, to rapidly spin around the opponent and inevitably rain down on them with a vicious onslaught from every direction, \nfilling the sky with a blinding light and inflicting a massive amount of damage.",
    'Hakai': "Used by Gods of Destruction to completely erase one from existance.",
    'Sphere of Destruction' : "In the film and manga, Beerus creates two medium-size flaming energy spheres in his hands and brings them above his head to create one single energy sphere resembling the Sun, which he throws at his opponent. ",
    'Temporal Do-Over' : "Whis has the ability to travel back in time up to three minutes in the past, allowing him to undo any events that occurred with the only ones around his vicinity to be fully aware of this.",
    'Strike of Revealation' : "The user swiftly karate chops the opponent on the neck, rendering them unconscious.",
    'Death Beam' : "To perform the technique, the user extends his right arm and fires a small, thin, very fast and concentrated laser-like beam of ki from his index finger, which barrels down and pierces through the opponent.",
    'Supernova' : "The user raises his finger and gathers their energy in the form of a giant yellow-orange, sun-like energy sphere.",
    'Absorption' : "The technique involves either engulfing a victim completely, or using a part of their body to suck the victim into their body, thus gaining their power and abilities.",
    'God Slicer' : "Goku Black creates a pink sword of energy from his Super Saiyan Rosé aura, which he then uses in combat.",
    'Heavenly Arrow' : 'Zamasu creates a field of purple energy around his right hand, creating a blade powerful enough to bifurcate a much bigger being.',
    'Time Skip' : 'The user skips time.',
    'Time Prison' : "Ensnares the enemy's movements by keeping them suspended in time.",
    'Power Impact': 'The user pulls their hand back, charging a red energy blast, and then pushes their hand forward, firing the attack.',
    'Energy Punch': 'A powerful punch charged with Ki.',
    'Barrier Punch': 'Android 17 forms a small barrier around his fist to increase the power of his punches.',
    'Android Barrier': "A technique where energy is thrust out from the body in the form of a barrier with great force. \nThe barrier can be used to both defend against oncoming projectiles and to expand and damage its surroundings.",
    'Wolf Fang Fist': "Yamcha typically does a combo of clawing and punching, then finishing with a double palm strike to launch his opponent away. \nHis hand and finger movements may be intended to mimic the biting of a wolf.",
    'Telekinesis': "A technique that allows the user to manipulate objects and other people with the power of one's mind.",
    'Invisible Eye Blast': "a Kiai technique shot from the eyes.",
    "Light Grenade": "The user puts their hands together in front of them as they charge a yellow energy sphere in their hands. \nThen, they bring their hands forward and fires the energy sphere, inflicting a massive amount of damage.",
}


def directory():
    info = input('Enter character: ')

    if info == Goku.name:
        Goku.intro()
        a = input('Techniques or Transformations? ')
        if a == "Techniques":
            print(Goku.techniques)
            b = input('Which technique do you want to know about? ')
            if b == Goku.techniques[0]:
                print(techniques['Kamehameha'])
            elif b == Goku.techniques[1]:
                print(techniques['Kaioken'])
        elif a == 'Transformations':
            print(Goku.transformations)
            c = input('Which transformation would you like more information on? ')
            if c == Goku.transformations[0]:
                print(ss_forms['Super Saiyan'])
            elif c == Goku.transformations[1]:
                print(ss_forms['Super Saiyan 2'])
            elif c == Goku.transformations[2]:
                print(ss_forms['Super Saiyan 3'])
            elif c == Goku.transformations[3]:
                print(ss_forms['Super Saiyan God'])
            elif c == (Goku.transformations[4]):
                print(ss_forms['Super Saiyan Blue'])
            elif c == (Goku.transformations[5]):
                print(ss_forms['Ultra Instinct: Omen'])
            elif c == (Goku.transformations[6]):
                print(ss_forms['Ultra Instinct: Mastered'])

    if info == Vegeta.name:
        Vegeta.intro()
        a = input('Techniques or Transformations? ')
        if a == "Techniques":
            print(Vegeta.techniques)
            b = input('Which technique do you want to know about? ')
            if b == (Vegeta.techniques[0]):
                print(techniques['Big Bang Attack'])
            elif b == (Vegeta.techniques[1]):
                print(techniques['Final Flash'])
        elif a == 'Transformations':
            print(Vegeta.transformations)
            c = input('Which transformation would you like more information on? ')
            if c == (Vegeta.transformations[0]):
                print(Vegeta.transformations[0])
                print(ss_forms['Super Saiyan'])
            elif c == (Vegeta.transformations[1]):
                print(Vegeta.transformations[1])
                print(ss_forms['Super Saiyan 2'])
            elif c == (Vegeta.transformations[2]):
                print(Vegeta.transformations[2])
                print(ss_forms['Super Saiyan God'])
            elif c == (Vegeta.transformations[3]):
                print(Vegeta.transformations[3])
                print(ss_forms['Super Saiyan Blue'])
            elif c == (Vegeta.transformations[4]):
                print(Vegeta.transformations[4])
                print(ss_forms['Super Saiyan Blue Evolution'])

    if info == Broly.name:
        Broly.intro()
        a = input('Techniques or Transformations? ')
        if a == "Techniques":
            print(Broly.techniques)
            b = input('Which technique do you want to know about? ')
            if b == (Broly.techniques[0]):
                print(techniques['Eraser Cannon'])
            elif b == (Broly.techniques[0]):
                print(techniques['Gigantic Catastrophe'])
        elif a == 'transformations':
            print(Broly.transformations)
            c = input('Which transformation would you like more information on? ')
            if c == (Broly.techniques[0]):
                print(ss_forms['Super Saiyan'])
            elif c == (Broly.techniques[1]):
                print(ss_forms['Super Saiyan'])
            elif c == (Broly.techniques[2]):
                print(ss_forms['Legendary Super Saiyan Saiyan'])

    if info == Gohan.name:
        Gohan.intro()
        a = input('Techniques or Transformations? ')
        if a == "Techniques":
            print(Gohan.techniques)
            b = input('Which technique do you want to know about? ')
            if b == (Gohan.techniques[0]):
                print(techniques['Kamehameha'])
            elif b == (Gohan.techniques[1]):
                print(techniques['Masenko'])
        elif a == 'Transformations':
            print(Gohan.transformations)
            c = input('Which transformation would you like more information on? ')
            if c == (Gohan.transformations[0]):
                print(ss_forms['Super Saiyan'])
            elif c == (Gohan.transformations[1]):
                print(ss_forms['Super Saiyan 2'])
            elif c == (Gohan.transformations[2]):
                print(ss_forms['Mystic Form'])

    if info == Trunks.name:
        Trunks.intro()
        a = input('Techniques or Transformations? ')
        if a == "Techniques":
            print(Trunks.techniques)
            b = input('Which technique do you want to know about? ')
            if b == (Trunks.techniques[0]):
                print(techniques['Burning Attack'])
            elif b == (Trunks.techniques[1]):
                print(techniques['Galick Gun'])
            elif b == (Trunks.techniques[2]):
                print(techniques['Final Flash'])
        elif a == 'Transformations':
            print(Trunks.transformations)
            c = input('Which transformation would you like more information on? ')
            if c == (Trunks.transformations[0]):
                print(ss_forms['Super Saiyan'])
            elif c == (Trunks.transformations[1]):
                print(ss_forms['Super Saiyan 2'])
            elif c == (Trunks.transformations[2]):
                print(ss_forms['Super Saiyan Rage'])

    if info == Goten.name:
        Goten.intro()
        a = input('Techniques or Transformations? ')
        if a == "Techniques":
            print(Goten.techniques)
            b = input('Which technique do you want to know about? ')
            if b == (Goten.techniques[0]):
                print(techniques['Kamehameha'])
        elif a == 'Transformations':
            print(Goten.transformations)
            c = input('Which transformation would you like more information on? ')
            if c == (Goten.transformations[0]):
                print(ss_forms['Super Saiyan'])

    if info == Cabba.name:
        Cabba.intro()
        a = input('Techniques or Transformations? ')
        if a == "Techniques":
            print(Cabba.techniques)
            b = input('Which technique do you want to know about? ')
            if b == (Cabba.techniques[0]):
                print(techniques['Galick Cannon'])
        elif a == 'Transformations':
            print(Cabba.transformations)
            c = input('Which transformation would you like more information on? ')
            if c == (Cabba.transformations[0]):
                print(ss_forms['Super Saiyan'])
            elif c == (Cabba.transformations[1]):
                print(ss_forms['Super Saiyan 2'])

    if info == Caulifla.name:
        Caulifla.intro()
        a = input('Techniques or Transformations? ')
        if a == "Techniques":
            print(Caulifla.techniques)
            b = input('Which technique do you want to know about? ')
            if b == (Caulifla.techniques[0]):
                print(techniques['Crush Cannon'])
            elif b == (Caulifla.techniques[1]):
                print(techniques['Burst of Energy'])
        elif a == 'Transformations':
            print(Caulifla.transformations)
            c = input('Which transformation would you like more information on? ')
            if c == (Caulifla.transformations[0]):
                print(Caulifla.transformations[0])
                print(ss_forms['Super Saiyan'])
            elif c == (Caulifla.transformations[1]):
                print(Caulifla.transformations[1])
                print(ss_forms['Super Saiyan 2'])

    if info == Kale.name:
        Kale.intro()
        a = input('Techniques or Transformations? ')
        if a == "Techniques":
            print(Kale.techniques)
            b = input('Which technique do you want to know about? ')
            if b == (Kale.techniques[0]):
                print(techniques['Gigantic Impact'])
            elif b == (Kale.techniques[1]):
                print(techniques['Blaster Meteor'])
        elif a == 'Transformations':
            print(Kale.transformations)
            c = input('Which transformation would you like more information on? ')
            if c == (Kale.transformations[0]):
                print(ss_forms['Super Saiyan'])
            elif c == (Kale.transformations[1]):
                print(ss_forms['Super Saiyan 2'])

    if info == Gogeta.name:
        Gogeta.intro()
        a = input('Techniques or Transformations? ')
        if a == "Techniques":
            print(Gogeta.techniques)
            b = input('Which technique do you want to know about? ')
            if b == (Gogeta.techniques[0]):
                print(techniques['Stardust Breaker'])
            elif b == (Gogeta.techniques[1]):
                print(techniques['Punisher Drive'])
        elif a == 'Transformations':
            print(Gogeta.transformations)
            c = input('Which transformation would you like more information on? ')
            if c == (Gogeta.transformations[0]):
                print(ss_forms['Super Saiyan'])
            elif c == (Gogeta.transformations[1]):
                print(ss_forms['Super Saiyan 2'])
            elif c == (Gogeta.transformations[2]):
                print(ss_forms['Super Saiyan God'])
            elif c == (Gogeta.transformations[3]):
                print(ss_forms['Super Saiyan Blue'])

    if info == Vegetto.name:
        Vegetto.intro()
        a = input('Techniques or Transformations? ')
        if a == "Techniques":
            print(Vegetto.techniques)
            b = input('Which technique do you want to know about? ')
            if b == (Vegetto.techniques[0]):
                print(techniques['Spirit Sword'])
            elif b == (Vegetto.techniques[1]):
                print(techniques['Big Bang Kamehameha'])
        elif a == 'Transformations':
            print(Vegetto.transformations)
            c = input('Which transformation would you like more information on? ')
            if c == (Vegetto.transformations[0]):
                print(ss_forms['Super Saiyan'])
            elif c == (Vegetto.transformations[1]):
                print(ss_forms['Super Saiyan 2'])
            elif c == (Vegetto.transformations[2]):
                print(ss_forms['Super Saiyan God'])
            elif c == (Vegetto.transformations[3]):
                print(ss_forms['Super Saiyan Blue'])

    if info == Kefla.name:
        Kefla.intro()
        a = input('Techniques or Transformations? ')
        if a == "Techniques":
            print(Kefla.techniques)
            b = input('Which technique do you want to know about? ')
            if b == (Kefla.techniques[0]):
                print(techniques['Ray Blast'])
            elif b == (Kefla.techniques[1]):
                print(techniques['Gigantic Blast'])
        elif a == 'Transformations':
            print(Kefla.transformations)
            c = input('Which transformation would you like more information on? ')
            if c == (Kefla.transformations[0]):
                print(ss_forms['Super Saiyan'])
            elif c == (Kefla.transformations[1]):
                print(ss_forms['Super Saiyan 2'])

    if info == Tien.name:
        Tien.intro()
        print(Tien.techniques)
        a = input('Which technique do you want to know about? ')
        if a == (Tien.techniques[0]):
            print(techniques['Tri-Beam'])
        elif a == (Tien.techniques[1]):
            print(techniques['Multi Form'])

    if info == Krillin.name:
        Krillin.intro()
        print(Krillin.techniques)
        a = input('Which technique do you want to know about? ')
        if a == (Krillin.techniques[0]):
            print(Krillin.techniques[0])
            print(techniques['Kamehameha'])
        elif a == (Krillin.techniques[0]):
            print(Krillin.techniques[1])
            print(techniques['Kienzan'])

    if info == Yamcha.name:
        Yamcha.intro()
        print(Yamcha.techniques)
        a = input('Which technique do you want to know about? ')
        if a == (Yamcha.techniques[0]):
            print(techniques['Kamehameha'])
        elif a == (Yamcha.techniques[1]):
            print(techniques['Wolf Fang Fist'])


    if info == a17.name:
        a17.intro()
        print(a17.techniques)
        a = input('Which technique do you want to know about? ')
        if a == (a17.techniques[0]):
            print(techniques['Barrier Punch'])
        elif a == (a17.techniques[1]):
            print(techniques['Android Barrier'])

    if info == a18.name:
        a18.intro()
        print(a18.techniques)
        a = input('Which technique do you want to know about? ')
        if a == (a18.techniques[0]):
            print(techniques['Kienzan'])
        elif a == (a18.techniques[1]):
            print(techniques['Energy Attack'])

    if info == Piccolo.name:
        Piccolo.intro()
        print(Piccolo.techniques)
        a = input('Which technique do you want to know about? ')
        if a == (Piccolo.techniques[0]):
            print(techniques['Makankosappo'])
        elif a == (Piccolo.techniques[1]):
            print(techniques['Hellzone Grenade'])
        elif a == (Piccolo.techniques[2]):
            print(techniques['Light Grenade'])

    if info == Beerus.name:
        Beerus.intro()
        print(Beerus.techniques)
        a = input('Which technique do you want to know about? ')
        if a == (Beerus.techniques[0]):
            print(techniques['Hakai'])
        elif a == (Beerus.techniques[1]):
            print(techniques['Sphere of Destruction'])

    if info == Whis.name:
        Whis.intro()
        print(Whis.techniques)
        a = input('Which technique do you want to know about? ')
        if a == (Whis.techniques[0]):
            print(techniques['Temporal Do-Over'])
        elif a == (Whis.techniques[1]):
            print(techniques['Strike of Revealation'])

    if info == Shin.name:
        Shin.intro()
        print(Shin.techniques)
        a = input('Which technique do you want to know about? ')
        if a == (Shin.techniques[0]):
            print(techniques['Invisible Eye Blast'])
        elif a == (Shin.techniques[1]):
            print(techniques['Telekinesis'])



    if info == Freeza.name:
        Freeza.intro()
        a = input('Techniques or Transformations? ')
        if a == "Techniques":
            print(Freeza.techniques)
            b = input('Which technique do you want to know about? ')
            if b == (Freeza.techniques[0]):
                print(techniques['Final Flash'])
            elif b == (Freeza.techniques[1]):
                print(techniques['Final Flash'])
        elif a == 'Transformations':
            print(Freeza.transformations)
            c = input('Which transformation would you like more information on? ')
            if c == (Freeza.transformations[0]):
                print(freeza_forms['First Form'])
            elif c == (Freeza.transformations[1]):
                print(freeza_forms['Second Form'])
            elif c == (Freeza.transformations[2]):
                print(freeza_forms['Third Form'])
            elif c == (Freeza.transformations[3]):
                print(freeza_forms['Final Form'])
            elif c == (Freeza.transformations[4]):
                print(freeza_forms['100% Full Power'])
            elif c == (Freeza.transformations[5]):
                print(freeza_forms['Golden Freeza'])

    if info == Cell.name:
        Cell.intro()
        a = input('Techniques or Transformations? ')
        if a == "Techniques":
            print(Cell.techniques)
            b = input('Which technique do you want to know about? ')
            if b == (Cell.techniques[0]):
                print(techniques['Kamehameha'])
            elif b == (Cell.techniques[1]):
                print(techniques['Death Beam'])
        elif a == 'Transformations':
            print(Cell.transformations)
            c = input('Which transformation would you like more information on? ')
            if c == (Cell.transformations[0]):
                print(cell_forms['Imperfect Cell'])
            elif c == (Cell.transformations[1]):
                print(cell_forms['Semi-Perfect Cell'])
            elif c == (Cell.transformations[2]):
                print(cell_forms['Perfect Cell'])
            elif c == (Cell.transformations[3]):
                print(cell_forms['Super Perfect Cell'])

    if info == Buu.name:
        Buu.intro()
        a = input('Techniques or Transformations? ')
        if a == "Techniques":
            print(Buu.techniques)
            b = input('Which technique do you want to know about? ')
            if b == (Buu.techniques[0]):
                print(techniques['Kamehameha'])
            elif b == (Buu.techniques[1]):
                print(techniques['Absorption'])
        elif a == 'Transformations':
            print(Buu.transformations)
            c = input('Which transformation would you like more information on? ')
            if c == (Buu.transformations[0]):
                print(buu_forms['Innoocent Buu'])
            elif c == (Buu.transformations[1]):
                print(buu_forms['Evil Buu'])
            elif c == (Buu.transformations[2]):
                print(buu_forms['Super Buu'])
            elif c == (Buu.transformations[3]):
                print(buu_forms['Kid Buu'])
                
    if info == Zamasu.name:
        Zamasu.intro()
        a = input('Techniques or Transformations? ')
        if a == "Techniques":
            print(Zamasu.techniques)
            b = input('Which technique do you want to know about? ')
            if b == (Zamasu.techniques[0]):
                print(techniques['God Slicer'])
            elif b == (Zamasu.techniques[1]):
                print(techniques['Heavenly Arrow'])
        elif a == 'Transformations':
            print(Zamasu.transformations)
            c = input('Which transformation would you like more information on? ')
            if c == (Zamasu.transformations[0]):
                print(zamasu_forms['Goku Black'])
            elif c == (Zamasu.transformations[1]):
                print(zamasu_forms['Fused Zamasu'])

    if info == Hit.name:
        Hit.intro()
        print(Hit.techniques)
        a = input('Which technique do you want to know about? ')
        if a == (Hit.techniques[0]):
            print(techniques['Time Skip'])
        elif a == (Hit.techniques[1]):
            print(techniques['Time Prison'])

    if info == Jiren.name:
        Jiren.intro()
        print(Jiren.techniques)
        a = input('Which technique do you want to know about? ')
        if a == (Jiren.techniques[0]):
            print(techniques['Power Impact'])
        elif a == (Jiren.techniques[1]):
            print(techniques['Energy Punch'])


directory()
