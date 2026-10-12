\# Intelligent Software Bug Investigator



\*\*An Agentic RAG and MCP-Based Software Bug Investigation System\*\*



\## Overview



Intelligent Software Bug Investigator is an AI-powered software engineering project designed to help developers investigate software bugs by retrieving relevant source code, application logs, technical documentation, and bug reports.



The system uses Retrieval-Augmented Generation (RAG) to find relevant engineering evidence. The planned architecture extends this capability with AI agents and Model Context Protocol (MCP) tools to support structured, evidence-based bug investigation and root-cause analysis.





\## Problem Statement



Software bug investigation often requires developers to examine multiple sources of information manually. Source code, logs, documentation, and previous bug reports may be scattered across different locations, making it difficult to identify root causes efficiently.



This project explores how semantic retrieval and AI-assisted workflows can help developers locate relevant evidence and investigate software defects.



\## Current Features



\- FastAPI backend with a basic investigation endpoint.

\- Synthetic software engineering dataset containing source code, documentation, logs, and sample bug reports.

\- Text embeddings generated using Sentence Transformers (`all-MiniLM-L6-v2`).

\- Local vector storage and similarity search using Qdrant.

\- Semantic retrieval of relevant engineering documents.

\- Prototype Python code chunking using the Abstract Syntax Tree (AST) module.

\- Standalone tests for retrieval and code chunking.



\## Technology Stack



\- \*\*Language:\*\* Python

\- \*\*Backend:\*\* FastAPI

\- \*\*Embeddings:\*\* Sentence Transformers

\- \*\*Vector Database:\*\* Qdrant

\- \*\*Code Processing:\*\* Python AST

\- \*\*API Testing:\*\* FastAPI Swagger UI and Python test scripts

\- \*\*Version Control:\*\* Git and GitHub



\## Architecture



```text

Bug Description

&#x20;     |

&#x20;     v

Embedding Generation

&#x20;     |

&#x20;     v

Qdrant Similarity Search

&#x20;     |

&#x20;     v

Relevant Code, Logs and Documentation

&#x20;     |

&#x20;     v

Future: AI-Assisted Root Cause Analysis

&#x20;     |

&#x20;     v

Future: Evidence-Based Investigation Report

```



\## Project Structure



```text

AI-Engineering-Investigator/

├── backend/

│   ├── app/

│   │   ├── api/

│   │   │   └── routes/

│   │   ├── rag/

│   │   └── main.py

│   ├── requirements.txt

│   ├── test\_chunking.py

│   └── test\_retriever.py

├── data/

│   ├── code/

│   ├── documentation/

│   ├── logs/

│   └── sample\_bugs/

├── .gitignore

└── README.md

```



\## Getting Started



\### Prerequisites



\- Python 3.10 or a compatible version supported by the installed dependencies

\- Git



\### 1. Clone the repository



```bash

git clone https://github.com/YOUR-USERNAME/ai-engineering-investigator.git

cd ai-engineering-investigator

```



Replace `YOUR-USERNAME` with your GitHub username.



\### 2. Create and activate a virtual environment



On Windows:



```cmd

python -m venv venv

venv\\Scripts\\activate

```



\### 3. Install dependencies



```cmd

pip install -r backend/requirements.txt

```



\### 4. Start the FastAPI server



```cmd

cd backend

uvicorn app.main:app --reload

```



Open the API documentation at:



http://127.0.0.1:8000/docs



\### 5. Test the RAG prototype



With the required dependencies installed and the Qdrant index built, run the retrieval test from the backend directory:



```cmd

python test\_retriever.py

```



To rebuild the local index, run:



```cmd

python -m app.rag.build\_index

```



Run these commands from the `backend` directory. The index builder and local storage paths must match the configuration in the code.



\## Development Roadmap



\- \[x] Set up the FastAPI backend.

\- \[x] Create a synthetic engineering dataset.

\- \[x] Generate text embeddings.

\- \[x] Implement basic Qdrant similarity retrieval.

\- \[x] Prototype AST-based Python code chunking.

\- \[ ] Integrate code-aware chunking into the indexing pipeline.

\- \[ ] Connect RAG retrieval to the investigation API.

\- \[ ] Add an LLM for evidence-based root cause analysis.

\- \[ ] Implement MCP tools for engineering data sources.

\- \[ ] Build an agent workflow using LangGraph.

\- \[ ] Add evidence verification and structured investigation reports.

\- \[ ] Develop a frontend for submitting bugs and viewing results.

\- \[ ] Evaluate retrieval quality and investigation accuracy.



\## Current Status



The project is under active development. The semantic retrieval prototype and standalone code chunking test have been demonstrated. Full agent orchestration, MCP integrations, and automated root cause analysis are planned enhancements.



\## Author



Suvetha P T





