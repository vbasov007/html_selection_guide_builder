from error import Error
import pandas as pd
from collections import OrderedDict
from mylogger import mylog


def read_excel(file_name: str, replace_nan=None, sheet_name=0) -> (pd.DataFrame, Error):
    try:
        out = pd.read_excel(file_name, dtype=str, sheet_name=sheet_name)

        if replace_nan is not None:
            out.fillna(replace_nan, inplace=True)
            out.replace(to_replace='nan', value=replace_nan, inplace=True)
        return out, Error(None)
    except Exception as e:
        return None, Error(file_name + str(e))


def read_sheet_names(file_name: str) -> (list, Error):
    try:
        xl = pd.ExcelFile(file_name)
        return xl.sheet_names, Error(None)
    except Exception as e:
        return None, Error(file_name + str(e))


def write_excel(file_name: str,
                df,  # data frame or dict of data frames where sheet_name is key
                prompt=False,
                convert_strings_to_urls=True,
                sheet_name='Sheet1') -> Error:
    while True:
        try:
            if convert_strings_to_urls:
                writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
            else:
                writer = pd.ExcelWriter(file_name, engine='xlsxwriter', options={'strings_to_urls': False})

            if isinstance(df, pd.DataFrame):  # if this is single sheet
                df.to_excel(writer, index=False, sheet_name=sheet_name)

            else:  # must be a dict of sheets
                for sheet in df:
                    df[sheet].to_excel(writer, index=False, sheet_name=sheet)
                    mylog.debug("Adding sheet {0}".format(sheet))

            writer.save()

            return Error(None)

        except Exception as e:
            error = Error(e)
            if prompt:
                answer = input("Can't write file {0}. Try again? (y/n)".format(file_name))
                if answer.lower() == 'y':
                    continue
                else:
                    break
            else:
                break
    return error


def add_new_sheet_to_excel(new_sheet_name: str, file_name: str, df: pd.DataFrame, prompt=False,
                           convert_strings_to_urls=True, new_sheet_position='current') -> Error:
    if new_sheet_position not in ('first', 'last', 'current'):
        return Error('Undefined sheet insert position')

    sheet_list, error = read_sheet_names(file_name)
    if error:
        # file doesn't exist yet, try to create new
        mylog.warning("File {0} doesn't exist. Creating new".format(file_name))
        error = write_excel(file_name,
                            df,
                            prompt=prompt,
                            convert_strings_to_urls=convert_strings_to_urls,
                            sheet_name=new_sheet_name)
        return error
    else:
        # read all existing sheets
        excel_with_sheets_dict = OrderedDict()

        if new_sheet_position == 'first':
            excel_with_sheets_dict[new_sheet_name] = df

        for sheet in sheet_list:
            if new_sheet_position != 'current' and sheet == new_sheet_name:
                continue
            excel_with_sheets_dict[sheet], error = read_excel(file_name, replace_nan='', sheet_name=sheet)
            if error:
                mylog.error(error)

        if new_sheet_position == 'last':
            excel_with_sheets_dict[new_sheet_name] = df

        error = write_excel(file_name,
                            excel_with_sheets_dict,
                            prompt=prompt,
                            convert_strings_to_urls=convert_strings_to_urls)

        return error
