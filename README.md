# PCBuilderBR

## Funcionalidades Core

### 1. Seleção de Componentes
**Categorias obrigatórias:**
- Processador (CPU)
- Placa-mãe (Motherboard)
- Memória RAM
- Placa de vídeo (GPU)
- Armazenamento (SSD/HDD)
- Fonte de alimentação (PSU)
- Gabinete (Case)

**Categorias opcionais:**
- Cooler (CPU vem com stock cooler)
- Coolers adicionais (fans)
- Monitor
- Periféricos (teclado, mouse, headset)

**Interface de seleção:**
- Lista filtrada por marca, preço, especificações
- Cards com imagem, specs principais, preço
- Busca inteligente (ex: "rtx 4060" ou "ryzen 7600")
- Ordenação: menor preço, melhor performance, mais popular
- Badges: "Melhor custo-benefício", "Mais escolhido", "Promoção"

### 2. Validação de Compatibilidade em Tempo Real

**Regras técnicas implementadas:**

**CPU ↔ Motherboard:**
- Socket match (AM5, AM4, LGA1700, LGA1200)
- Chipset suportado
- BIOS update warnings (ex: Ryzen 7000 em placa B550)

**RAM ↔ Motherboard:**
- Tipo DDR (DDR4, DDR5)
- Velocidade máxima suportada
- Capacidade máxima (slots disponíveis)
- Dual/Quad channel otimizado

**GPU ↔ Case:**
- Comprimento máximo suportado
- Clearance warnings (GPU muito grande para gabinete)

**PSU ↔ Componentes:**
- TDP total calculado (CPU + GPU + periféricos)
- Margem de segurança 20-30%
- Conectores necessários (8-pin, 6-pin para GPU)
- Certificação recomendada (80+ Bronze mínimo)

**Cooler ↔ Case:**
- Altura máxima do cooler vs clearance do gabinete
- Compatibilidade com socket

**Feedback visual:**
- ✅ Verde: Compatível
- ⚠️ Amarelo: Atenção (funciona mas não ideal)
- ❌ Vermelho: Incompatível (bloqueia finalização)


### Funcionalidades
- Opções dos produtos mais vendidos do mercado (MVP)
- Soma de preços dos produtos escolhidos (MVP)
- Analise de compatibilidade entre as peças (MVP)

- Preços dos produtos nas principais lojas, atualizados a cada semana via Web Scraping (MVP)
- Performance aproximada da config nos jogos mais famosos
- Links para cada um dos produtos com as melhores ofertas
- Historico de preços de cada produto em cada loja
- Compartilhar configs por link 
- Salvar a config como csv ou JSON
- Builds prontas recomendadas
- Calculo de consumo para validar fonte de energia

### Stack
- Frontend: React, react-hook-form-zod, axios, vite, tailwindCSS
- Backend: FastAPI, RabbitMQ(async scraping job), Selenium, Docker, PostgreSQL, Pydantic
