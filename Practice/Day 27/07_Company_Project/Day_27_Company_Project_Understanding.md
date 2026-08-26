# Day 27 — Assigned Company Project Understanding

## Project: AI Customer Support Agent

## 1. Project Overview

The assigned AI project is an AI Customer Support Agent designed to assist customers by answering their questions using company-provided knowledge.

The project uses Artificial Intelligence and Retrieval-Augmented Generation (RAG) concepts to retrieve relevant information from a knowledge base and generate context-aware responses.

The project aims to reduce repetitive customer support workload, improve response time, and provide consistent information to users.

---

## 2. Business Requirements

The main business requirements identified for the project are:

- Provide automated assistance for common customer queries.
- Reduce repetitive work for human customer support teams.
- Provide fast responses to customer questions.
- Use company-approved information as the primary knowledge source.
- Reduce the risk of unsupported AI responses.
- Provide a fallback mechanism for queries that cannot be reliably answered.
- Allow the knowledge base to be updated as company information changes.
- Maintain a scalable architecture for future improvements.

---
## Practical Requirements Understanding

The project requirements were reviewed from both business and technical perspectives.

### Business Problem

Customer support teams often receive repetitive questions that require information already available in company documents. An AI Customer Support Agent can automate these common queries and reduce repetitive manual effort.

### Target Users

The primary users are:

- Customers seeking information or assistance.
- Customer support teams handling unresolved or escalated queries.

### Inputs

The primary input is a natural-language customer question.

Examples:

- Product-related questions
- Service-related questions
- Policy-related questions
- Account or support-related questions

### Outputs

The expected output is a clear and relevant AI-generated response based on information available in the company knowledge base.

### Key Requirement

The most important requirement is that the AI should provide responses based on reliable company information and should not confidently provide unsupported information.

### Practical Requirement Flow

Customer Query
↓
Query Processing
↓
Knowledge Retrieval
↓
Relevant Information
↓
AI Response Generation
↓
Customer Response

If reliable information is unavailable:

Customer Query
↓
Knowledge Retrieval
↓
No Reliable Information
↓
Fallback / Escalation
↓
Human Support

## 3. Functional Requirements

The AI Customer Support Agent should:

1. Accept customer questions through a support interface.
2. Process natural-language customer queries.
3. Search the company knowledge base.
4. Retrieve relevant information using semantic search.
5. Provide retrieved information as context to the LLM.
6. Generate a relevant and understandable response.
7. Avoid presenting unsupported information as a reliable answer.
8. Handle unknown or unsupported queries through a fallback mechanism.
9. Escalate unresolved requests to human support when required.

---

## 4. Technical Requirements

The planned technical components include:

| Component | Purpose |
|---|---|
| Python | Application and AI pipeline development |
| LLM | Natural-language response generation |
| Embedding Model | Convert text into vector representations |
| Vector Database | Store and retrieve document embeddings |
| RAG | Connect knowledge retrieval with LLM response generation |
| Git/GitHub | Version control and collaboration |
| Testing Framework/Tools | Validate system functionality and AI responses |

The exact technologies may be adjusted based on project requirements and deployment constraints.

---

## 5. Project Architecture

The planned architecture follows a Retrieval-Augmented Generation workflow.

### High-Level Flow

Customer
↓
Customer Support Interface
↓
Query Processing
↓
Retriever
↓
Vector Database
↓
Relevant Knowledge
↓
LLM
↓
Generated Response
↓
Customer

### Knowledge Base Flow

Company Documents
↓
Document Loader
↓
Document Chunking
↓
Embedding Model
↓
Vector Database

### Fallback Flow

Customer Query
↓
Knowledge Base Search
↓
Relevant Information Available?
├── Yes → LLM → Response → Customer
└── No → Fallback → Human Support

---
## Practical Architecture Understanding

The project architecture was reviewed by identifying the major components involved in processing a customer query and generating an AI response.

### 1. Customer Support Interface

The customer submits a question through the support interface.

**Input:** Natural-language customer query

**Output:** Query forwarded to the AI processing layer.

### 2. Query Processing

The query is prepared for the retrieval system.

The system identifies the user's question and prepares it for semantic search against the knowledge base.

### 3. Retriever

The retriever searches the knowledge base for information relevant to the customer query.

Its purpose is to identify the most useful document chunks that can be provided as context to the LLM.

### 4. Vector Database

The vector database stores the embeddings generated from company knowledge documents.

It enables semantic similarity search so that relevant information can be retrieved even when the customer's wording differs from the wording used in the source document.

### 5. LLM

The Large Language Model receives the customer query together with the retrieved context.

It generates a natural-language response based on the available information.

### 6. Response Generation

The generated answer is returned to the customer through the support interface.

The response should remain grounded in the retrieved company information.

### 7. Fallback and Escalation

If relevant and reliable information cannot be retrieved, the system should avoid generating an unsupported answer.

Instead, the request can be handled through a fallback response or escalated to a human support team.

### Practical Data Flow

Customer
↓
Support Interface
↓
Query Processing
↓
Retriever
↓
Vector Database
↓
Relevant Context
↓
LLM
↓
Response Generation
↓
Customer

### Knowledge Processing Flow

Company Documents
↓
Document Loader
↓
Document Chunking
↓
Embedding Model
↓
Vector Database

### Architecture Understanding Outcome

The architecture was understood as a modular pipeline where document processing prepares the knowledge base, retrieval identifies relevant information, and the LLM uses the retrieved context to generate the final response.

The modular design also allows individual components to be improved or replaced without redesigning the entire system.

## 6. Knowledge Base and RAG Workflow

The knowledge base is prepared from company-related documents.

The planned workflow is:

1. Load company documents.
2. Split documents into smaller chunks.
3. Generate embeddings for the chunks.
4. Store embeddings in a vector database.
5. Convert the customer query into an embedding.
6. Retrieve the most relevant document chunks.
7. Pass retrieved context to the LLM.
8. Generate a grounded response.
9. Return the response to the customer.

This approach helps the AI system answer questions using relevant company information instead of relying only on general model knowledge.

---

## 7. Sprint Planning

The project can be organized into three major sprints.

### Sprint 1 — Foundation

**Goal:** Build the knowledge and technical foundation.

Tasks:

- Requirements analysis
- Architecture design
- Prepare company knowledge documents
- Document loading
- Document chunking
- Embedding generation
- Vector database setup
- Initial retrieval testing

**Expected Output:**

A searchable company knowledge base ready for AI retrieval.

---

### Sprint 2 — AI Agent Development

**Goal:** Build the working AI customer support workflow.

Tasks:

- Retrieval implementation
- RAG pipeline development
- LLM integration
- Prompt design
- Response generation
- Customer support interface
- Fallback mechanism
- Support escalation workflow

**Expected Output:**

A functional AI Customer Support Agent capable of answering customer questions using retrieved company knowledge.

---

### Sprint 3 — Testing and Delivery

**Goal:** Validate and prepare the system for delivery.

Tasks:

- Create test cases
- Test retrieval accuracy
- Evaluate AI responses
- Test unsupported queries
- Test edge cases
- Fix identified issues
- Complete documentation
- Prepare deployment configuration

**Expected Output:**

A tested, documented, and deployment-ready AI Customer Support Agent.

---
## Practical Sprint Tasks Understanding

The project was divided into manageable sprint tasks based on technical dependencies and business value.

### Sprint 1 — Foundation

**Sprint Goal:** Establish the project and knowledge-base foundation.

| Task | Complexity | Priority | Dependency |
|---|---|---|---|
| Requirements analysis | Low | P0 | None |
| Architecture design | Medium | P0 | Requirements |
| Knowledge document preparation | Medium | P0 | Requirements |
| Document loading | Medium | P0 | Knowledge Documents |
| Document chunking | Medium | P0 | Document Loading |
| Embedding generation | Medium | P0 | Chunking |
| Vector database setup | Medium | P0 | Embeddings |

**Sprint Outcome:**

A structured and searchable knowledge base is prepared for the AI system.

---

### Sprint 2 — AI Agent Development

**Sprint Goal:** Develop the core AI customer-support workflow.

| Task | Complexity | Priority | Dependency |
|---|---|---|---|
| Retrieval implementation | High | P0 | Vector Database |
| RAG pipeline | High | P0 | Retrieval |
| LLM integration | Medium | P0 | RAG |
| Prompt design | Low | P1 | LLM Integration |
| Response generation | Medium | P0 | LLM Integration |
| Customer support interface | Medium | P1 | Response Generation |
| Fallback and escalation | Medium | P1 | Response Generation |

**Sprint Outcome:**

A functional AI Customer Support Agent is available for customer queries.

---

### Sprint 3 — Testing and Delivery

**Sprint Goal:** Validate the AI system and prepare it for delivery.

| Task | Complexity | Priority | Dependency |
|---|---|---|---|
| Test case creation | Low | P0 | Core System |
| Retrieval accuracy testing | High | P0 | Retrieval |
| AI response evaluation | High | P0 | Response Generation |
| Edge-case testing | Medium | P0 | Core System |
| Issue resolution | Medium | P0 | Testing |
| Documentation | Low | P1 | Completed System |
| Deployment preparation | High | P2 | Testing |

**Sprint Outcome:**

The project is tested, documented, and prepared for future deployment.

---

## Sprint Task Execution Approach

Tasks are executed according to their dependencies.

Foundation tasks are completed first because later AI components depend on them. Retrieval and RAG are treated as critical tasks because they directly affect the quality of AI responses.

Testing is performed after the core workflow becomes functional so that retrieval accuracy, response quality, and edge cases can be evaluated.

### Task Tracking

Each sprint task can be tracked using the following status categories:

- **To Do** — Task has not started.
- **In Progress** — Task is currently being developed.
- **Review** — Development is complete and the task is under review.
- **Testing** — Task is being validated.
- **Done** — Task has been completed and verified.

### Sprint Review Considerations

At the end of each sprint, the team should review:

- Completed tasks
- Incomplete tasks
- Blockers
- Technical issues
- Testing results
- Changes required for the next sprint
- Progress toward the sprint goal

## 8. Sprint Task Prioritization

Tasks are prioritized according to business value and technical dependencies.

### P0 — Critical

- Requirements analysis
- Architecture design
- Knowledge base preparation
- Document processing
- Embeddings
- Vector database
- Retrieval
- RAG pipeline
- LLM integration
- Response generation
- Testing and evaluation
- Critical issue resolution

### P1 — Important

- Prompt refinement
- Customer support interface
- Fallback and escalation
- Project documentation

### P2 — Future

- Production deployment improvements
- Advanced monitoring
- Performance optimization
- Additional features

---

## 9. Team Roles

A collaborative AI project requires multiple roles.

| Role | Responsibility |
|---|---|
| Product Owner | Defines business requirements and priorities |
| Scrum Master | Manages Agile process and removes blockers |
| AI/ML Developer | Develops RAG, embeddings, retrieval, prompts, and LLM integration |
| Backend Developer | Develops APIs and application logic |
| Frontend Developer | Develops the customer support interface |
| QA/Test Engineer | Tests functionality, retrieval, and AI responses |
| DevOps Engineer | Handles deployment and environment configuration |
| Technical Writer | Maintains project documentation |

For a smaller team, one person may handle multiple responsibilities.

---

## 10. Team Workflow

The planned Agile workflow is:

Requirements
↓
Product Backlog
↓
Sprint Planning
↓
Task Assignment
↓
Development
↓
Code Review
↓
Testing
↓
Bug Fixing
↓
Sprint Review
↓
Delivery

Team members communicate progress, discuss blockers, review work, and coordinate dependencies throughout the sprint.

---
## Practical Team Workflow Understanding

The project workflow was structured around Agile development principles. The workflow connects business requirements, sprint planning, development, Git collaboration, testing, and delivery.

### 1. Requirement Discussion

The project begins by identifying the business problem and defining the expected functionality.

The Product Owner or project stakeholder provides requirements and priorities.

### 2. Backlog Creation

Requirements are converted into manageable tasks and added to the project backlog.

Each task can be evaluated based on:

- Business value
- Complexity
- Priority
- Dependencies
- Expected output

### 3. Sprint Planning

The team selects appropriate tasks from the backlog for the upcoming sprint.

The team discusses:

- Sprint goal
- Task priority
- Complexity
- Dependencies
- Task ownership
- Expected deliverables

### 4. Task Assignment

Tasks are assigned to team members based on their roles and technical responsibilities.

For example:

| Role | Example Responsibility |
|---|---|
| AI/ML Developer | RAG, embeddings, retrieval, LLM integration |
| Backend Developer | APIs and application logic |
| Frontend Developer | Customer support interface |
| QA Engineer | Testing and evaluation |
| DevOps Engineer | Deployment and environment setup |

### 5. Development

Team members work on their assigned tasks using separate Git feature branches.

Development is performed according to the sprint requirements and project architecture.

### 6. Git Collaboration

The development workflow follows:

```text
Feature Branch
↓
Development
↓
Testing
↓
Commit
↓
Push
↓
Pull Request
↓
Code Review
↓
Approval
↓
Merge

## 11. Git Collaboration Workflow

The project uses a feature-branch based Git workflow.

```text
main
├── feature/rag-pipeline
├── feature/llm-integration
├── feature/customer-support-ui
├── feature/fallback-system
└── feature/testing
Development Workflow
main
↓
Create Feature Branch
↓
Development
↓
Testing
↓
Commit
↓
Push
↓
Pull Request
↓
Code Review
↓
Approval
↓
Merge into main

Example:

git checkout main
git pull origin main

git checkout -b feature/rag-pipeline

git add .
git commit -m "Implement RAG pipeline"

git push -u origin feature/rag-pipeline

The Pull Request is reviewed before merging the changes into the main branch.

12. Testing Workflow

The planned testing process includes:

Functional Testing

Verify that:

Customer queries are accepted.
Documents are loaded correctly.
Retrieval works correctly.
Responses are generated.
Fallback handling works.
Retrieval Testing

Verify whether the system retrieves relevant document chunks for different customer questions.

Response Evaluation

Evaluate responses based on:

Accuracy
Relevance
Grounding
Completeness
Consistency
Edge-Case Testing

Test:

Unknown questions
Empty queries
Irrelevant questions
Ambiguous questions
Queries outside the knowledge base
13. Project Timeline
Phase	Timeline	Major Output
Foundation	Weeks 1–3	Knowledge base and retrieval foundation
AI Development	Weeks 4–5	Working AI Customer Support Agent
Testing & Delivery	Week 6	Tested and documented system
14. Expected Project Outcome

The expected outcome is a functional AI Customer Support Agent capable of:

Understanding customer questions.
Retrieving relevant company information.
Generating context-aware responses.
Handling unsupported questions safely.
Escalating unresolved requests.
Supporting future expansion of the company knowledge base.
15. Day 27 Learning Outcome

Through this project planning exercise, the following concepts were applied:

Agile methodology
Sprint planning
Task complexity estimation
Business-value prioritization
Dependency analysis
Architecture design
Team role definition
Git collaboration
Code review workflow
Testing strategy
Project timeline planning

The project was structured into manageable sprints to demonstrate how an AI project can be planned and developed using Agile principles.

16. Project Status

Planning Status: Completed

Architecture Design: Completed

Sprint Planning: Completed

Task Prioritization: Completed

Team Role Definition: Completed

Git Collaboration Workflow: Documented

Testing Strategy: Planned

Company-Specific Implementation Details: To be updated when additional project requirements or instructions are provided.