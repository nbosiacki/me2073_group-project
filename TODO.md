# Campus Marketplace — Task Tracker

## Phase 1: Project Scaffolding, Git, and Tooling
- [x] Create mono-repo directory structure (backend/, frontend/, scripts/)
- [x] Initialize Git with .gitignore (Claude files, node_modules, venv, .env)
- [x] Set up Python venv with FastAPI, Motor, pytest, etc.
- [x] Create backend health endpoint with test
- [x] Scaffold React app with Vite
- [x] Configure Vitest + React Testing Library
- [x] Create .env.example with documented env vars
- [x] Create TODO.md
- [x] Verify all tests pass and make initial commit

## Phase 2: Database Models and Schema
- [ ] Design User Pydantic models (UserCreate, UserInDB, UserResponse)
- [ ] Design Posting Pydantic models (PostingCreate, PostingInDB, PostingResponse)
- [ ] Create GeoLocation model for map coordinates
- [ ] Define enums: PostingCategory, PostingStatus, ItemCondition
- [ ] Set up Motor async DB connection (database.py)
- [ ] Create MongoDB indexes (geospatial, text, unique)
- [ ] Write model validation tests (12-15 tests)
- [ ] Write database connection tests

## Phase 3: Backend API Core — CRUD
- [ ] Implement posting CRUD endpoints (GET, POST, PUT, DELETE)
- [ ] Implement GET /api/postings/nearby (geo query)
- [ ] Implement user CRUD endpoints
- [ ] Implement GET /api/users/:id/postings
- [ ] Add pagination support (page, limit params)
- [ ] Add category filtering and sort options
- [ ] Create service layer (posting_service, user_service)
- [ ] Write integration tests for all endpoints (~35 tests)

## Phase 4: Authentication and User Management
- [ ] Implement POST /api/auth/register (bcrypt password hashing)
- [ ] Implement POST /api/auth/login (JWT token generation)
- [ ] Implement GET /api/auth/me
- [ ] Implement POST /api/auth/refresh
- [ ] Create get_current_user FastAPI dependency
- [ ] Add authorization (users edit/delete only own postings)
- [ ] Update Phase 3 tests with auth headers
- [ ] Write auth tests (~20 tests)

## Phase 5: Frontend Foundation, Routing, and Layout
- [ ] Set up React Router (/, /login, /register, /profile/:id, /postings/new, /postings/:id)
- [ ] Create Layout shell (Navbar, Footer)
- [ ] Create shared UI components (Button, Card, Input, Modal, LoadingSpinner, ErrorMessage)
- [ ] Set up Axios API client with JWT interceptor
- [ ] Create AuthContext with localStorage persistence
- [ ] Build LoginPage and RegisterPage
- [ ] Write component and page tests (~22 tests)

## Phase 6: Main Page — Map + Posting Feed
- [ ] Integrate React-Leaflet with OpenStreetMap tiles
- [ ] Create MapView component with posting markers
- [ ] Create PostingFeed (scrollable card list, right 25%)
- [ ] Create PostingCard component
- [ ] Synchronize map markers with feed cards (click interaction)
- [ ] Create usePostings hook for data fetching
- [ ] Add loading skeletons and empty states
- [ ] Write tests (~15 tests)

## Phase 7: Posting Creation and Management UI
- [ ] Build PostingForm (title, description, category, price, condition, location, images, tags)
- [ ] Build LocationPicker (click-on-map to set coordinates)
- [ ] Build ImageUpload with preview
- [ ] Build PostingDetailPage (full info, images, author, contact)
- [ ] Implement edit posting (pre-filled form)
- [ ] Implement delete posting with confirmation
- [ ] Build backend image upload endpoint (POST /api/uploads)
- [ ] Write tests (~20 tests)

## Phase 8: User Profiles and Inter-User Features
- [ ] Build ProfilePage (/profile/:id) with user info and postings
- [ ] Build ProfileEditForm
- [ ] Design Message model (Pydantic + MongoDB)
- [ ] Implement messaging API (POST/GET /api/messages)
- [ ] Build inbox page with conversation threads
- [ ] Build message thread view
- [ ] Add read/unread status
- [ ] Write tests (~16 tests)

## Phase 9: Search, Filtering, and Categories
- [ ] Add SearchBar to navbar (debounced)
- [ ] Build FilterPanel (category checkboxes, price range, condition)
- [ ] Build SortDropdown (newest, price asc/desc)
- [ ] Create SearchContext for shared filter state
- [ ] Enhance backend GET /api/postings with q, category, price, condition, sort_by params
- [ ] Implement MongoDB $text search + query builder
- [ ] Sync filters to URL params for shareable links
- [ ] Write tests (~22 tests)

## Phase 10: Dev Tools, Dummy Data, Polish, and Deployment
- [ ] Create scripts/seed_users.py (50 dummy users via Faker)
- [ ] Create scripts/seed_postings.py (200 dummy postings with campus coords)
- [ ] Create scripts/seed_all.py (orchestrator)
- [ ] Create scripts/seed_config.py (campus coords, building names, category weights)
- [ ] Create Dockerfiles for backend and frontend
- [ ] Create docker-compose.yml (MongoDB + backend + frontend)
- [ ] Add ErrorBoundary and EmptyState components
- [ ] Add responsive breakpoints (mobile: stacked layout)
- [ ] Configure CORS for production
- [ ] Final README with setup instructions
- [ ] Final test suite run (~180 tests total)
