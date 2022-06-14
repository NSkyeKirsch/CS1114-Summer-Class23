def rhyme(flower1="Roses", flower2="Violets", color1="red", color2="blue", ending="So there's that"):
    print("{} are {}.".format(flower1, color1))
    print("{} are {}.".format(flower2, color2))
    print("{}.".format(ending))
    print()


def main():
    rhyme("Sunflower", "Tulips", "yellow", "purple", "Sugar is sweet, and so are you")
    rhyme("Roses", "Violets", "red", "blue", "I like you, but let's just be friends for now...")
    rhyme("Roses", "Violets")
    rhyme("Roses", "Violets", color2="orange")
    rhyme()


if __name__ == "__main__":
    main()
