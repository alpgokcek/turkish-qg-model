# MEF University Senior Design Thesis/Project Report LaTeX Template 
LaTeX Template for Computer Engineering Senior Design Report (Bachelor’s) @MEFUniversity

This template imitates the ubiquitous MS Word version. Main motive was not to deal with horrendous and error-prone formatting of the MS Word and being able to work collaboratively with group mates on different operating systems simultaneously.

This template provides rough structure while defining  the environment styling. Therefore, you can solely focus on the content instead of hassling with the trivial stuff.

_BEWARE: This template has not been rigorously tested. Some edge cases may or may not cause unexpected issues or formatting errors. Also, always have a backup of your work! preferably version control._

## Can I use it?
This template had been developed considering the majority of users would be novices about LaTex. Hence, page structure, formatting and styling is being handeled at the background while the user only provides the content. 

If you are completely stranger to LaTeX, it’s pretty straightforward and easy to learn. You’ll get more comfortable as you use it.

## How do I use it?
You can simply start by cloning this repository and modify the files. If you choose not to do so, or couldn’t understand the structure, detailed explanatation is given below.

Create your `.tex` file and make sure you have the `mefsdp.cls` under the same directory or move it where  your `TEXMFHOME` variable points to.

I recommend using the folder structure in this repository. Where the bibliography, source files and figures are seperated. 

Begin your `.tex` file with 

```
\documentclass{mefsdp}
```
Section of the file between the `\documentclass{mefsdp}`and `begin{document}`is called preamble. In the preamble; you must define the variables that will be used throughtout the document. **Make sure you declare all of them**. Here is the full list with examples:

- `\setauthors{Jony Ive, Charles Eames, Don Norman}`
- `\settitle{title of the design project goes here in all capital letters}`
- `\setcourseno{I}` % set I or II
- `\setmonth{January}`
- `\setyear{2020}`
- `\setfaculty{Engineering}` % it adds `Faculty of` in front
- `\setdepartment{Computer Engineering}` % it append `Department`
- `\setchair{Prof. Charles Eames}` % include academic titles
- `\setdate{\today}` % any day
- `\setadvisor{Assoc. Prof. Steve Wozniak}` % include academic titles
- `\settitleTR{konu başlığı hepsi büyük harf olacak şekilde buraya yazılır eğer başlık çok uzunsa otomatik olarak yeni satıra geçilir}`
- `\setmonthTR{Ocak}`
- `\setfacultyTR{Mühendislik}`
- `\setdepartmentTR{Bilgisayar Mühendisliği}`
- `\setadvisorTR{Doç. Dr. Steve Wozniak}`

After these, you must define path variable for the figures (or any other name) directory.
- `\setfigurepath{../figures/}`

### Begin typing your document
As you know, you write your report in the `document` environment. After declaring the variables, you may begin your `document`. 

_You must execute the enumerated steps in the exact order! Examples can be seen from the [source file](source/report.tex)._

1- **After the  `\begin{document}` first line must be `\makestandards`**
It makes all of the essential pages such as cover page, acceptence, honesty pledge etc. 

2- **Begin abstract environment**
Write your abstract in English. Use `\keywords` command _in this environment only_ if you have any. Write your keywords as comma seperated list.

3- **Begin abstractTR environment**
Write your abstract in Turkish. Use `\anahtarkelimeler` command _in this environment only_ if you have any. Comma seperated as well.

4- **After completing the abstracts in both languages, first line must be `\makestandards`**
It makes all of the listings such as list of figures, list of tables, table of contents and list of abbreviations.


It’s up to you after this point. `section`, `subsection` and `subsubsection` environments has been redefined in the template according to suggested styling. By default, when you start a new section it automatically adds a page break. You can override this setting by passing ‘nobreak’ as option to section environment
```
\begin[nobreak]{section}
	FILL HERE
\end{section}
```  

* Adding abbreviations to your document
	We utilize the _glossaries_ package for this task. As the package suggests, you must define the abbreviations and their full text in the preamble before using them. The syntax is as follows:
```
\newacronym{_label_}{_acronym_}{_full text_}
% example
\newacronym{svm}{SVM}{Support Vector Machines}
```
You must reference these by using the `\gls[_label_]` command in the text

* Appendix Environment
There are `Appendix` environment defined for adding the miscellaneous content to your report. Usage is almost same with any other environment. However, you should specifiy the identifier of the appendix by passing it as an option to the environment.
```
\begin{abstract}[A]
	CONTENT OF APPENDIX A
\end{abstract}

\begin{abstract}[B]
	CONTENT OF APPENDIX B
\end{abstract}

```
One more environment is the `acknowledgments`. There is not any arguments specific to this environment. Simply you open it with
```
\begin{acknowledgments}
	Special thanks to…
\end{acknowledgments}
```

Finally, `bibliography`. There is not any adjustments on the bibliography. You choose your style and pass the relative path of the `.bib` file as in;
```
	\bibliographystyle{apalike}
	\bibliography{../bibliography/references}
```

