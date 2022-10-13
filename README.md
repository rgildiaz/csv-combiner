# csv-combiner

A simple utility for combining CSVs!

Written for PMG Python Challenge - Fall 2022

## Usage

```bash
$ python ./csv-combiner.py [OPTIONS] FILES [...FILES]
```

### Combine files

```bash
$ python ./csv-combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv
```

Given two input files named `clothing.csv` and `accessories.csv`:

| email_hash                                                       | category  |
| ---------------------------------------------------------------- | --------- |
| 21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63      | Shirts    |
| 21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63      | Pants     |
| 166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b | Cardigans |

| email_hash                                                       | category |
| ---------------------------------------------------------------- | -------- |
| 176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab | Wallets  |
| 63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe | Purses   |

csv-combiner outputs:

| email_hash                                                       | category  | filename        |
| ---------------------------------------------------------------- | --------- | --------------- |
| 21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63      | Shirts    | clothing.csv    |
| 21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63      | Pants     | clothing.csv    |
| 166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b | Cardigans | clothing.csv    |
| 176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab | Wallets   | accessories.csv |
| 63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe | Purses    | accessories.csv |

csv-combiner can also combine more than two files.

### Drop duplicates

To drop duplicates in the output CSV, use the `-d` option:

```bash
$ python ./csv-combiner.py ./fixtures/accessories1.csv ./fixtures/accessories2.csv -d > combined.csv
```

Given two input files named `accessories1.csv` and `accessories2.csv`:

| email_hash                                                       | category |
| ---------------------------------------------------------------- | -------- |
| 21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63      | Satchels |
| 63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe | Purses   |

| email_hash                                                       | category |
| ---------------------------------------------------------------- | -------- |
| 176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab | Wallets  |
| 63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe | Purses   |

csv-combiner outputs:

| email_hash                                                       | category | filename         |
| ---------------------------------------------------------------- | -------- | ---------------- |
| 21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63      | Satchels | accessories1.csv |
| 63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe | Purses   | accessories1.csv |
| 176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab | Wallets  | accessories2.csv |
