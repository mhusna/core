# Core Calculators

Business uygulamaları tarafından kullanılan ortak hesaplama helper'ları.

## Geliştirme ve test

```powershell
python -m pip install -e ".[test]"
python -m pytest
```

`calculate_total(items)` verilen tutarların toplamını döndürür. Bu demo
`v0.1.0` sürümünü yayımlar; bağımlı business uygulaması bu tag'i kullanır.
Core'daki her push etki analizi workflow'unu çalıştırır.
