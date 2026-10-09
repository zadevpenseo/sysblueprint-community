-- ========================================================================
-- SYSBLUEPRINT SHOWCASE: ENTERPRISE MULTI-TIER PROCUREMENT SYSTEM
-- Dialect: ANSI SQL-92 / PostgreSQL 15+
-- ========================================================================

CREATE TABLE "departments" (
    "id" UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    "code" VARCHAR(32) NOT NULL UNIQUE,
    "name" VARCHAR(128) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "procurement_requests" (
    "id" UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    "dept_id" UUID NOT NULL,
    "title" VARCHAR(255) NOT NULL,
    "total_amount" NUMERIC(14,2) NOT NULL CHECK ("total_amount" > 0),
    "current_status" VARCHAR(32) NOT NULL DEFAULT 'draft',
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "fk_procurement_dept" FOREIGN KEY ("dept_id") 
        REFERENCES "departments" ("id") ON DELETE RESTRICT
);

CREATE TABLE "approval_audits" (
    "id" BIGSERIAL PRIMARY KEY,
    "request_id" UUID NOT NULL,
    "approver_role" VARCHAR(64) NOT NULL,
    "decision" VARCHAR(32) NOT NULL,
    "notes" TEXT,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "fk_audit_request" FOREIGN KEY ("request_id") 
        REFERENCES "procurement_requests" ("id") ON DELETE CASCADE
);

CREATE INDEX "idx_procurement_dept_status" ON "procurement_requests" ("dept_id", "current_status");
CREATE INDEX "idx_audit_request_created" ON "approval_audits" ("request_id", "created_at");
