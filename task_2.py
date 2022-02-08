import pandas as pd
def get_xrates(year_from, year_to=None, month_from=1, month_to=None,
               cur='dollar-ssha'):
    url_pat='https://www.calc.ru/kotirovka-{}.html?date={}-{:02}'
    year_to = year_to or year_from
    month_to = month_to or month_from
    dfs = []
    for y in range(year_from, year_to+1):
        for m in range(month_from, month_to+1):
            df = (pd.read_html(url_pat.format(cur, y, m), skiprows=1)[1]
                    .rename(columns={0:'date', 1:'xrate'}))
            df['date'] = pd.to_datetime(df['date'], dayfirst=True)
            dfs.append(df)
    return pd.concat(dfs, ignore_index=True).sort_values('date')