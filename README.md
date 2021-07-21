# Paper

This repository contains the main paper accompanying
[sid](https://github.com/covid-19-impact-lab/sid), an epidemiological model.

The current published version is available as an [arXiv
preprint](https://arxiv.org/abs/2106.11129). Please cite it with

```
@misc{Gabler2021,
      title={
        The Effectiveness of Strategies to Contain SARS-CoV-2: Testing,
        Vaccinations, and NPIs
      },
      author={
        Janoś Gabler and Tobias Raabe and Klara Röhrl
        and Hans-Martin von Gaudecker
      },
      year={2021},
      eprint={2106.11129},
      archivePrefix={arXiv},
      primaryClass={q-bio.PE}
}
```


## Versions

- v1 - 2020-11-25

  The first version of the paper was published to accompany Dorn et al. (2020).

- v2 - 2020-12-20

  The second version of the paper was published to accompany Gabler, Raabe, Röhrl, von
  Gaudecker (2020).

- v3 - 2021-02-09

  An updated version for the CRC Discussion Series.

- v4 - 2021-06-22

  The fourth version in this repository corresponds to the second version of the
  pre-print published on arXiv.


## Related publications

Here is a list of related publications.

- Dorn, F., Gabler, J., von Gaudecker, H. M., Peichl, A., Raabe, T., & Röhrl, K. (2020).
  [Wenn Menschen (keine) Menschen treffen: Simulation der Auswirkungen von
  Politikmaßnahmen zur Eindämmung der zweiten
  Covid-19-Welle](https://www.ifo.de/publikationen/2020/aufsatz-zeitschrift/wenn-menschen-keine-menschen-treffen-simulation).
  ifo Schnelldienst Digital, 1(15).

- Gabler, J., Raabe, T., Röhrl, K. & von Gaudecker, H. M. (2020). [Die Bedeutung
  individuellen Verhaltens über den Jahreswechsel für die Weiterentwicklung der
  Covid-19- Pandemie in Deutschland](http://ftp.iza.org/sp99.pdf). IZA Standpunkte Nr.
  99.

- Gabler, J., Raabe, T., Röhrl, K., & Gaudecker, H. M. V. (2021). [Der Effekt von
  Heimarbeit auf die Entwicklung der Covid-19-Pandemie in
  Deutschland](http://ftp.iza.org/sp100.pdf) (No. 100). Institute of Labor Economics
  (IZA).


## Development

Here are some useful things to know.

- Uncomment the following line in ``paper/preamble.tex`` to remove all comments from the
  compiled paper.

  ```latex
  % \PassOptionsToPackage{final}{changes}
  ```

- Register yourself as a commentator with your own color in ``paper/preamble.tex`` as
  seen here:

  ```latex
  \definechangesauthor[name={Tobias}, color=alizarin]{T}
  ```

  Then, comment or propose a replacement or deletion with

  ```latex
  \comment[id=T]{<some-comment>}
  \delete[id=T]{<comment>}{<to-be-deleted>}
  \replaced[id=T]{<comment>}{<to-be-replaced>}
  ```


## Notes for Updating the arXiv Version

1. Compile the document without comments, i.e. with `\PassOptionsToPackage{final}{changes}`.

2. Save the resulting `paper.bbl` file in the src folder where `paper.tex` is.

3. zip the src folder and upload it to archive.


If the run on arxive fails, the most likely culprits are:

- it used `tex` and not `pdflatex` in the command -> put `\pdfoutput=1` as first line
  of `paper.tex`

- everything before `\begin{document}` **must** be in the main paper without input
  statements.
