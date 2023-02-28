  # Out of the box
  processed 52923 tokens with 4351 phrases; found: 3323 phrases; correct: 2072.
accuracy:  92.43%; precision:  62.35%; recall:  47.62%; FB1:  54.00
              LOC: precision:  64.89%; recall:  66.67%; FB1:  65.76  1011
             MISC: precision:  41.00%; recall:  22.02%; FB1:  28.65  239
              ORG: precision:  61.42%; recall:  50.76%; FB1:  55.59  1405
              PER: precision:  68.11%; recall:  37.23%; FB1:  48.15  668
 # With is capital             
processed 52923 tokens with 4351 phrases; found: 4980 phrases; correct: 2781.
accuracy:  94.55%; precision:  55.84%; recall:  63.92%; FB1:  59.61
              LOC: precision:  55.35%; recall:  74.09%; FB1:  63.36  1317
             MISC: precision:  29.93%; recall:  28.31%; FB1:  29.10  421
              ORG: precision:  55.09%; recall:  62.76%; FB1:  58.67  1937
              PER: precision:  65.82%; recall:  70.29%; FB1:  67.99  1305
# With is capital and wordlen
processed 52923 tokens with 4351 phrases; found: 5174 phrases; correct: 2717.
accuracy:  94.18%; precision:  52.51%; recall:  62.45%; FB1:  57.05
              LOC: precision:  54.73%; recall:  71.75%; FB1:  62.09  1290
             MISC: precision:  20.33%; recall:  25.17%; FB1:  22.49  551
              ORG: precision:  52.77%; recall:  61.71%; FB1:  56.89  1988
              PER: precision:  63.20%; recall:  69.56%; FB1:  66.23  1345
# With is capital and punct
processed 52923 tokens with 4351 phrases; found: 4978 phrases; correct: 2781.
accuracy:  94.55%; precision:  55.87%; recall:  63.92%; FB1:  59.62
              LOC: precision:  55.32%; recall:  73.98%; FB1:  63.30  1316
             MISC: precision:  30.31%; recall:  28.54%; FB1:  29.40  419
              ORG: precision:  55.03%; recall:  62.71%; FB1:  58.62  1937
              PER: precision:  65.85%; recall:  70.38%; FB1:  68.04  1306
# With is capital and is_definite_article
processed 52923 tokens with 4351 phrases; found: 4980 phrases; correct: 2780.
accuracy:  94.55%; precision:  55.82%; recall:  63.89%; FB1:  59.59
              LOC: precision:  55.28%; recall:  73.98%; FB1:  63.28  1317
             MISC: precision:  29.93%; recall:  28.31%; FB1:  29.10  421
              ORG: precision:  55.06%; recall:  62.76%; FB1:  58.66  1938
              PER: precision:  65.87%; recall:  70.29%; FB1:  68.01  1304
# With is capital and is_num
processed 52923 tokens with 4351 phrases; found: 5031 phrases; correct: 2824.
accuracy:  94.69%; precision:  56.13%; recall:  64.90%; FB1:  60.20
              LOC: precision:  55.36%; recall:  73.98%; FB1:  63.33  1315
             MISC: precision:  32.93%; recall:  36.63%; FB1:  34.68  495
              ORG: precision:  55.30%; recall:  62.88%; FB1:  58.85  1933
              PER: precision:  67.08%; recall:  70.70%; FB1:  68.84  1288

<h2>Classifier test_sent</h2>

# With is capital and is_num: F-Score is 64.78wor
processed 51533 tokens with 3558 phrases; found: 4077 phrases; correct: 2473.
accuracy:  96.05%; precision:  60.66%; recall:  69.51%; FB1:  64.78
              LOC: precision:  67.86%; recall:  71.68%; FB1:  69.72  1145
             MISC: precision:  29.69%; recall:  31.27%; FB1:  30.46  357
              ORG: precision:  57.54%; recall:  69.79%; FB1:  63.07  1698
              PER: precision:  69.90%; recall:  83.40%; FB1:  76.05  877


# test_set
processed 51533 tokens with 3558 phrases; found: 3457 phrases; correct: 2663.
accuracy:  96.63%; precision:  77.03%; recall:  74.85%; FB1:  75.92
              LOC: precision:  80.55%; recall:  72.97%; FB1:  76.57  982
             MISC: precision:  65.07%; recall:  43.95%; FB1:  52.46  229
              ORG: precision:  75.56%; recall:  79.07%; FB1:  77.28  1465
              PER: precision:  78.87%; recall:  83.81%; FB1:  81.27  781

# dev set
