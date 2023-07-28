# High level interface: List[Program]

from dataclasses import dataclass, field
from typing import List

@dataclass
class ProgramCode:
    hesa: List[str] = None                # If uni says the program code is HESA code
    ucas: List[str] = None                # If uni says the program code is UCAS code, could be a list https://www.bayes.city.ac.uk/study/undergraduate/courses/accounting-and-finance
    universityCode: List[str] = None      # If uni just provide a code without explanation

@dataclass
class Course:
    credits: float = None           # 30 or 7.5 https://www.ucl.ac.uk/module-catalogue/modules/behaviouralscience-MSIN0239
    description: str = None         # Full description of course as a string
    ilos: List[str] = None          # Intended Learing Outcomes / Learning Outcomes , if provided
    name: str = None                # Introduction to Financial Accounting
    optional: bool = None           # Compulsory or optional course 
    originalName: str = None        # Introduction to Financial Accounting (30 credits)
    period: int = None              # Provided as a year by university, i.e. "Year 1" -> 1
    source: str = None              # link to a page the data is scraped from

@dataclass
class Qualification:
    description: str = None         # Any additional info provided
    legalEntity: str = None         # University name
    name: str = None                # Program name
    qualificatoinLevel: str = None  # MSc / MBA / BA Hons / BA / PHD etc

@dataclass
class Program:
    code: ProgramCode = None
    name: str = None                                       # Medicines Optimisation, PGCert/PGDip/MSc
    partTime: bool = None                                  # Does program offer part-time mode
    homePrice: int = None                                  # Price for home students
    overseasPrice: int = None                              # Price for international students
    sandwich: bool = None                                  # Sandwich course is the one offering a year of work placement/study abroad
    source: str = None                                     # link to a page the data is scraped from
    courses: List[Course] = field(default_factory=list)   
    qualifications: List[Qualification] = field(default_factory=list) # Medicines Optimisation, PGCert/PGDip/MSc -> [PGCert, PGDip, MSc]
