from setuptools import setup

setup(
    name='colorful_figlet',
    version="0.1",
    description="Beautifull colorful figlet for python prgram with terminal",
    long_description="""
    figlet(text,font,color) -> figlet("text",big","red")
    color and font are optional -> figlet(text)
    return figlet form of text that you give to input
    show_colors() -> return list of colors you can use
    show_fonts() -> return list of fonts you can use
    """,
    url="https://github.com/Mahdi-Shafiei-IRAN/colorful_figlet",
    author="MAHDI",
    author_email="mahdishafiei920@gmail.com",
    license="MIT",
    install_requires=['termcolor','pyfiglet'],
    packages=['colorful_figlet'],
    zip_safe=False,
)
