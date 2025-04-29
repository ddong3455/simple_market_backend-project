# 🛒 Simple Market - 중고거래 백엔드 API

> **JWT 인증 기반의 중고거래 플랫폼 백엔드**  
> 실무 환경을 고려한 API 설계, 사용자 인증, 상품 거래 흐름 구현

---

## 📌 프로젝트 개요

- **목표**: 중고 거래에 필요한 핵심 기능(회원 관리, 상품 등록, 거래 확정)을 구현하고, RESTful API 설계 및 JWT 인증을 통한 실무 대응력을 갖추는 것
- **역할**: 기획, 모델 설계, API 개발, JWT 인증, Postman 테스트, GitHub 정리까지 전 과정 100% 단독 수행
- **기술 스택**: `Django`, `Django REST Framework`, `SimpleJWT`, `SQLite`, `Postman`, `Git`

---

## 💡 주요 기능

| 분류 | 기능 설명 |
|:--|:--|
| 회원 | 회원가입 / 로그인 (JWT 인증) |
| 상품 | 상품 등록 / 조회 / 수정 / 삭제 |
| 거래 | 상품 예약 / 구매 확정 |
| 마이페이지 | 내가 등록한 상품 / 내가 예약한 상품 목록 확인 |
| 테스트 | Postman Collection 제공 (깃허브 포함) |

---

## 🧩 API 설계

> RESTful 기준에 맞게 설계하였으며, JWT 토큰을 통한 인증이 필요합니다.

### ✅ 인증 (JWT)

| 메서드 | URL | 설명 |
|--------|-----|------|
| POST | `/users/signup/` | 회원가입 |
| POST | `/users/login/` | 로그인 (access, refresh 토큰 발급) |

### 🛍️ 상품

| 메서드 | URL | 설명 |
|--------|-----|------|
| POST | `/products/create/` | 상품 등록 |
| GET | `/products/list/` | 상품 목록 |
| GET | `/products/{id}/` | 상품 상세 조회 |
| PUT | `/products/{id}/update/` | 상품 수정 |
| DELETE | `/products/{id}/delete/` | 상품 삭제 |
| PATCH | `/products/{id}/reserve/` | 상품 예약 |
| PATCH | `/products/{id}/confirm/` | 구매 확정 |
| GET | `/products/mypage/` | 마이페이지 (내 상품/예약 상품) |

---

## 🧪 Postman 테스트

- `New Collection.postman_collection.json` 포함됨
- Import 후 JWT 토큰으로 인증 테스트 가능  
- 요청 예시 스크린샷 및 응답 결과도 함께 첨부

---

## 🔐 인증 방식

- 로그인 시 `access token` / `refresh token` 발급
- 모든 상품 API 요청 시 아래 헤더 필요:

```http
Authorization: Bearer {access_token}
