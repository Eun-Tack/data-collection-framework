# projects/

수집 실행은 주제별 폴더로 격리합니다. 새 수집은 `_TEMPLATE/`를 복사해 시작하세요.

## 구조
```
projects/{주제}/
├── COLLECTION_SPEC.md            # P0 산출물 (SSOT)
├── phase1_discovery/00_Source_Manifest.md
├── phase2_collect/<track>_Collection.md
├── phase3_vet/00_Vetting_Report.md
└── phase4_catalog/00_Catalog.md · manifest.csv · 02_Synthesis.md
```

## 시작
1. `_TEMPLATE/` → `{주제}/`로 복사.
2. collection-scoper로 `COLLECTION_SPEC.md` 작성·Lock (P0).
3. Phase 순서대로 진행. 각 Phase Gate 통과 후 다음 단계.
