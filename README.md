# Paper

This repository contains the technical paper describing
[sid](https://github.com/covid-19-impact-lab/sid).

The current published version is available as an [IZA discussion
paper](https://www.iza.org/publications/dp/13899).


## Related publications

Here is a list of publications which rely on sid.

- Dorn, F., Gabler, J., von Gaudecker, H. M., Peichl, A., Raabe, T., & Röhrl, K. (2020).
  [Wenn Menschen (keine) Menschen treffen: Simulation der Auswirkungen von
  Politikmaßnahmen zur Eindämmung der zweiten
  Covid-19-Welle](https://www.ifo.de/publikationen/2020/aufsatz-zeitschrift/wenn-menschen-keine-menschen-treffen-simulation).
  ifo Schnelldienst Digital, 1(15).


## Versions

- v1 - 2020-11-25

  The first version of the paper was published to accompany Dorn et al. (2020).


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
  \replace[id=T]{<comment>}{<to-be-replaced>}
  ```
