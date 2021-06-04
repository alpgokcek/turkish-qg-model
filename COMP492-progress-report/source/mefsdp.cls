\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{mefsdp}[2020/12/08 MEF University Senior Design Project Report Template]

\LoadClass[12pt]{report}

\RequirePackage{graphicx}
\RequirePackage{amsmath}
\RequirePackage{indentfirst}
\RequirePackage{titlecaps}
\RequirePackage[T1]{fontenc}
\RequirePackage{ifthen}
\RequirePackage[center,labelfont=bf,labelsep=endash]{caption}
\RequirePackage{natbib}
\RequirePackage[hidelinks]{hyperref}
\RequirePackage{tabularx}
\RequirePackage[ddmmyyyy]{datetime}
\RequirePackage{xstring}
\RequirePackage[nomain,acronym]{glossaries} % must be imported after hyperref


% Font Sizes
% \normalsize	12pt
% \large		14.4pt
% \Large		17.28pt


% user is expected to define these variables in premable
\newcommand{\settitle}[1]{\def\@projecttitle{#1}}
\newcommand{\setauthors}[1]{\def\@authors{#1}} % be aware of the internal \@author
\newcommand{\setmonth}[1]{\def\@projectmonth{#1}}
\newcommand{\setyear}[1]{\def\@projectyear{#1}}
\newcommand{\setdate}[1]{\def\@projectdate{#1}} % dd/mm/yyyy
\newcommand{\setcourseno}[1]{\def\@courseno{#1}}
\newcommand{\setfaculty}[1]{\def\@faculty{Faculty of #1}}
\newcommand{\setdepartment}[1]{\def\@department{Department of #1}}
\newcommand{\setchair}[1]{\def\@departmentchair{#1}}
\newcommand{\setadvisor}[1]{\def\@advisor{#1}}
\newcommand{\keywords}[1]{\def\@keywords{#1}}

\newcommand{\settitleTR}[1]{\def\@projecttitleTR{#1}}
\newcommand{\setmonthTR}[1]{\def\@projectmonthTR{#1}}
\newcommand{\setfacultyTR}[1]{\def\@facultyTR{#1 Fakültesi}}
\newcommand{\setdepartmentTR}[1]{\def\@departmentTR{#1 Bölümü}}
\newcommand{\setadvisorTR}[1]{\def\@advisorTR{#1}}
\newcommand{\anahtarkelimeler}[1]{\def\@anahtarkelimeler{#1}}

\newcommand{\setfigurepath}[1]{\def\@figpath{#1}}
\graphicspath{\@figpath}

% create metadata for output pdf 
\AtBeginDocument{
\hypersetup{
	pdfauthor={\@authors},
	pdftitle={\titlecap \@projecttitle},
	pdfsubject={MEF University Senior Design Project Report}
	}
}

% set numbering of section headers
\renewcommand\thesection{\arabic{section}.}
\renewcommand\thesubsection{\thesection\arabic{subsection}.}
\renewcommand\thesubsubsection{\thesubsection\arabic{subsubsection}.}

% enable numbering on subsubsection headers
\addtocounter{secnumdepth}{1}
% include subsections in toc
\addtocounter{tocdepth}{1}

% section header style w/ page break
\newcommand{\@secstylebr}{\newpage\centering\large\bfseries\scshape}

% section header style wo/ page break
\newcommand{\@secstylenobr}{\centering\large\bfseries\scshape}

% set header text and style for toc, references, lof and lot
\newcommand{\@headerstyle}{\vspace{-3em}\@secstylenobr}
\renewcommand{\contentsname}{\@headerstyle Table of Contents}
\renewcommand{\bibname}{\@headerstyle References}
\renewcommand{\listfigurename}{\@headerstyle List of Figures}
\renewcommand{\listtablename}{\@headerstyle List of Tables}


% style for in-text abbreviations
\setacronymstyle{long-short}
\makenoidxglossaries
% width of the description column at list of abbreviations page
\setlength{\glsdescwidth}{.8\textwidth}
% abbreviations are shown in bold at list of abbreviations page
\renewcommand{\glsnamefont}[1]{\textbf{#1}}

%\let\@tocsecformat\l@section
%\let\@tocsubsecformat\l@subsection
%\let\@tocsubsubsecformat\l@subsubsection
%\renewcommand\l@section {\titlecaps \@tocsecformat}
%\renewcommand\l@subsection {\titlecaps \@tocsecformat}
%\renewcommand\l@subsubsection{\titlecaps \@tocsecformat}
	

% words not be capitalized in title case
\Addlcwords{a, an, by, to, the, of, and, but, for, in, on, is}


\renewcommand\section[1][]{
	\ifthenelse{\equal{#1}{nobreak}}
	{\let\@secstyle\@secstylenobr}{\let\@secstyle\@secstylebr}
	\@startsection
	{section}{1}{0mm} % name, level, indent
	{-1\baselineskip} % beforeskip
	{0.5\baselineskip} % afterskip
	{\@secstyle}
}

\renewcommand\subsection{\@startsection
	{subsection}{2}{0mm} % name, level, indent
	{-1\baselineskip} % beforeskip
	{0.5\baselineskip} % afterskip
	{\bfseries \titlecap} % style
}

\renewcommand\subsubsection{\@startsection
	{subsubsection}{3}{0mm} % name, level, indent
	{-1\baselineskip} % beforeskip
	{0.5\baselineskip} % afterskip
	{\bfseries \titlecap} % style
}


% user sets the authors as comma seperated list.
% in order to align and centeralize the authors, we utilize the built-in \and command from the report class
% simply, we substite 'comma followed by a space' with \and 
\expandarg % necessary for accessing the contents of \@authors 
\newcommand{\@authorstab}{\StrSubstitute[0]{\@authors}{, }{\and}}

\newcommand{\@coverpage}{
	\clearpage
	\thispagestyle{empty}{
	\centering
	\bfseries
		\includegraphics[width=0.3\textwidth]{\@figpath mef_logo.png}\\
		\vspace{8em}
		{\Large \MakeUppercase{\@projecttitle} \par}
		\vspace{6em}
		Senior Design Project \@courseno \\
		\vspace{6em}
		{
			\begin{tabular}[t]{c}
				\@authorstab
			\end{tabular}
		} 
		\vfill
		\begin{center}
			\@projectyear
		\end{center}
	}
}

\newcommand{\@descriptivetitle}{
	\clearpage
	\thispagestyle{empty}{
	\centering
	\bfseries
	MEF UNIVERSITY \\ \MakeUppercase{\@faculty} \\
	\vspace{1em}
	\MakeUppercase{\@department} \\
	\vspace{6em}
	{\Large \MakeUppercase{\@projecttitle} \par}
			\vspace{4em}
	Senior Design Project \@courseno \\
	\vspace{4em}
	{
		\begin{tabular}[t]{c}
			\@authorstab
		\end{tabular}
	} \\
	\vspace{4em}
	Advisor: \@advisor \\
	\vfill
	\begin{center}
		\@projectyear
	\end{center}
	}
}

\newcommand{\@acceptancepage}{
	\clearpage
	\thispagestyle{empty}{
		\centering
		\bfseries
		MEF UNIVERSITY \\ \MakeUppercase{\@faculty} \par
		\vspace{1em}
		\MakeUppercase{\@department} \par
		\vspace{6em}
	}
	\begin{tabularx}{0.98\textwidth}{l X}
		Project Title &: {\titlecap \@projecttitle} \\
		Student(s) Name &: \@authors \\
		Date &: \@projectdate 
	\end{tabularx}
	\vspace{5em}
	
	I hereby state that the design project prepared by {\titlecap \@authors} has been completed under my supervision. I accept this work as a “Senior Design Project”.
	\vspace{1em}
	\begin{flushright}
		\@projectdate
		\par
		\@advisor
	\end{flushright}
	\vfill
	
	I hereby state that I have examined this senior design project by {\titlecap \@authors}. This work is acceptable as a “Senior Design Project”.
	\vspace{1em}
	\begin{flushright}
		\@projectdate
		\par
		\@departmentchair
		\par
		Head of the Department of
		\par Computer Engineering
		\par
	\end{flushright}
}

% tand is magical, don't remove!!
\newcommand{\tand}{&}
\newcommand{\@authorstlist}{\@for\tmp:=\@authors\do{\tmp \tand \@projectdate \tand \\ \\}}

\newcommand{\@honestypledge}{
	\clearpage
	\thispagestyle{empty}
	\begin{center}
		\bfseries
		\MakeUppercase{Academic Honesty Pledge}
	\end{center}
	\vspace{3em}
	In keeping with MEF University Student Code of Conduct, I pledge that this work is my own and that I have not received inappropriate assistance in its preparation. I further declare that all resources are explicitly cited. \newline \par 
	\begin{table}[h]
		\begin{tabularx}{\textwidth}{X X r}
			NAME & DATE & SIGNATURE\\
			\hline \\
			\@authorstlist
		\end{tabularx}
	\end{table}
	
}

\newcommand{\@listofabbreviations}{
	\clearpage
	\thispagestyle{empty}
	\printnoidxglossary[type=\acronymtype,title=\@headerstyle List of Abbreviations, style=long3col] % causing overfull hbox
}


\newcommand{\makestandards}{
	% it is customary to use roman literals for page numberings before the first section in the template
	\pagenumbering{roman} 
	
	\@coverpage
	\@descriptivetitle
	\@acceptancepage
	\@honestypledge

}

\newcommand{\makelists}{
	\tableofcontents
	\listoffigures
	\listoftables
	\@listofabbreviations
	
	% convert page numbering back to arabic numbers
	\cleardoublepage
	\pagenumbering{arabic}
}

\renewenvironment{appendix}[1][]{
	\begin{center}
		\@secstylebr Appendix #1
	\end{center}
	\addcontentsline{toc}{section}{APPENDIX #1}
	}
	{}


\newenvironment{acknowledgments}{
	\begin{center}
		\@secstylebr Acknowledgments
	\end{center}
	\addcontentsline{toc}{section}{ACKNOWLEDGMENTS}
	}
	{}


\renewenvironment{abstract}{
	{\centering
		{\@secstylebr ABSTRACT} \vspace{3em}
		
		\MakeUppercase{\@projecttitle} \par \vspace{1em}
		
		{
			\begin{tabular}[t]{c}
				\@authorstab
			\end{tabular}
		} \\ \vspace{1em}
		
		MEF UNIVERSITY \par
		\@faculty \par
		\@department \par \vspace{1em}
		Advisor: \@advisor  \par \vspace{1em}
		\MakeUppercase{\@projectmonth}, \@projectyear \par \vspace{3em}
	}
	\addcontentsline{toc}{section}{ABSTRACT}
}
{\vfill \textbf{\emph{Keywords:}} \@keywords}


\newenvironment{abstractTR}{
	{\centering
		{\@secstylebr ÖZET} \vspace{3em}
		
		\MakeUppercase{\@projecttitleTR} \par \vspace{1em}
		
		{
			\begin{tabular}[t]{c}
				\@authorstab
			\end{tabular}
		} \\ \vspace{1em}
		
		MEF ÜNİVERSİTESİ \par
		\@facultyTR \par
		\@departmentTR \par \vspace{1em}
		Tez Danışmanı: \@advisorTR  \par \vspace{1em}
		\MakeUppercase{\@projectmonthTR}, \@projectyear \par \vspace{3em}
	}
	\addcontentsline{toc}{section}{ÖZET}
}
{\vfill \textbf{\emph{Anahtar Kelimeler:}} \@anahtarkelimeler}
