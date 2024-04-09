import xmltodict
import pprint
import sys

# from tabulate import tabulate

# "\\cnhkg-ev-hudson\c$\jenkins\server\jobs\HL8_Dot23_V2\config.xml"
sConfigFilePointer = r'\\cnhkg-ev-hudson\c$\jenkins\server\jobs\%s\config.xml'

lsPlatform = []
lsPlatform.append('HL8_CMUX_V2')
lsPlatform.append('HL8_Dot0_V2')
lsPlatform.append('HL8_Dot10_V2')
lsPlatform.append('HL8_Dot11_V2')
lsPlatform.append('HL8_Dot12_V2')
lsPlatform.append('HL8_Dot15_V2')
lsPlatform.append('HL8_Dot16_V2')
lsPlatform.append('HL8_Dot18_V2')
lsPlatform.append('HL8_Dot1A_V2')
lsPlatform.append('HL8_Dot1B_V2')
lsPlatform.append('HL8_Dot21_V2')
lsPlatform.append('HL8_Dot22_V2')
lsPlatform.append('HL8_Dot23_V2')
lsPlatform.append('HL8_Dot24_V2')
lsPlatform.append('HL8_Dot25_V2')
lsPlatform.append('HL8_Dot2_V2')
lsPlatform.append('HL8_Dot3_V2')
lsPlatform.append('HL8_Dot4_V2')
lsPlatform.append('HL8_Dot5_V2')
lsPlatform.append('HL8_Dot7_V2')
lsPlatform.append('HL8_DotCMU_V2')


lsPlatformConfigFile = [sConfigFilePointer % sPlatform for sPlatform in lsPlatform]

ddPlatformParser = {}

# FIXME llaw, better to struct me up
# sPrintFormatter1 = '{HL8_Dot0_V2}'
lsTargetPrintFormatter = []
lsTargetPrintFormatter.append(u'UART1_COM')
lsTargetPrintFormatter.append(u'UART2_COM')
lsTargetPrintFormatter.append(u'SIM_INI')
lsTargetPrintFormatter.append(u'PowerSupply')
lsTargetPrintFormatter.append(u'AUX_COM')
lsTargetPrintFormatter.append(u'AUX_SIM_INI')
lsTargetPrintFormatter.append(u'PowerSupply_Tester')
lsTargetPrintFormatter.append(u'AUX2_COM')
lsTargetPrintFormatter.append(u'AUX2_SIM_INI')
lsTargetPrintFormatter.append(u'Module_Type')
lsTargetPrintFormatter.append(u'Module_Ref')
lsTargetPrintFormatter.append(u'QC_Path_Test_Campaign')
lsTargetPrintFormatter.append(u'QC_Filter')
lsTargetPrintFormatter.append(u'QC_status_filter')
lsTargetPrintFormatter.append(u'QC_test_name_filter')
lsTargetPrintFormatter.append(u'HARD_INI')
lsTargetPrintFormatter.append(u'SOFT_INI')
lsTargetPrintFormatter.append(u'AVMS_INI')
lsTargetPrintFormatter.append(u'AVMS_LOCAL_DELTA')
lsTargetPrintFormatter.append(u'Pre_Run')
lsTargetPrintFormatter.append(u'__TIMEOUT')
lsTargetPrintFormatter.append(u'QC_TESTPLAN_CONDITIONS_FILTER')
lsTargetPrintFormatter.append(u'assignedNode')


sPrintHeader = 'Platform\t' + '\t'.join('%s' % sTemp for sTemp in lsTargetPrintFormatter)
sPrintFormatter = '{:<1}\t' + '\t'.join('{%s}' % sTemp for sTemp in lsTargetPrintFormatter)

dORColumn = {}


def main():

    for sPlatform in lsPlatform:
        dPlatformParse = {}

        sConfigFile = sConfigFilePointer % sPlatform

        f = open(sConfigFile, 'r')
        sTemp = ''.join(f.readlines())

        dTemp = xmltodict.parse(sTemp)['project']
        sAssignedNode = xmltodict.parse(sTemp)['project']['assignedNode']

        # pprint.pprint(dTemp)
        # print(dTemp['properties']['hudson.model.ParametersDefinitionProperty']['parameterDefinitions']['hudson.model.StringParameterDefinition'])
        ldBuildParameters = []
        for sParaDef in ['hudson.model.StringParameterDefinition',
                         'hudson.model.ChoiceParameterDefinition',
                         'hudson.model.TextParameterDefinition',
                         ]:

            if sParaDef in dTemp['properties']['hudson.model.ParametersDefinitionProperty']['parameterDefinitions'].keys():
                ldBuildParameters += dTemp['properties']['hudson.model.ParametersDefinitionProperty']['parameterDefinitions'][sParaDef]
        # ldBuildParameters = dTemp['properties']['hudson.model.ParametersDefinitionProperty']['parameterDefinitions']['hudson.model.StringParameterDefinition']

        for dBuildParameters in ldBuildParameters:
            try:
                # FIXME dirty hack again
                if str(type(dBuildParameters)) == "<class 'collections.OrderedDict'>" and 'name' in dBuildParameters.keys():
                    # if dBuildParameters['name'] in lsTargetPrintFormatter:
                    if dBuildParameters['name'] not in dORColumn.keys() and dBuildParameters['name'] is not None:
                        # print 'name: %s' % dBuildParameters['name']
                        dORColumn[dBuildParameters['name']] = 1
                    if 'defaultValue' in dBuildParameters.keys():
                        dPlatformParse[dBuildParameters['name']] = dBuildParameters['defaultValue']
                    elif 'choices' in dBuildParameters.keys():
                        # FIXME llaw, dirty hack ahead
                        if type(dBuildParameters['choices']['a']['string']) == type(u''):
                            dPlatformParse[dBuildParameters['name']] = dBuildParameters['choices']['a']['string']
                        if type(dBuildParameters['choices']['a']['string']) == type([]):
                            dPlatformParse[dBuildParameters['name']] = dBuildParameters['choices']['a']['string'][0]
                    else:
                        print 'DEBUG: captain, i can\'t see shit!'
                        pass
                        # if sPlatform == 'HL8_Dot0_V2' and dBuildParameters['name'] == 'SIM_INI':
                        #     pprint.pprint(dBuildParameters)
                        #     sys.exit()
                pass

            except Exception as e:
                # print dBuildParameters['name']
                pprint.pprint(dBuildParameters)
                raise
            else:
                pass

        dPlatformParse['assignedNode'] = sAssignedNode

        ddPlatformParser[sPlatform] = dPlatformParse

    for sPlatform in ddPlatformParser.keys():
        dPlatformParse = ddPlatformParser[sPlatform]
        for sTargetPrintFormatter in dORColumn.keys():
            try:
                # print sTargetPrintFormatter
                if sTargetPrintFormatter in dPlatformParse.keys():
                    pass
                else:
                    dPlatformParse[sTargetPrintFormatter] = 'NaN'
                pass
            except Exception as e:
                pprint.pprint(dPlatformParse)
                raise
            else:
                pass
        ddPlatformParser[sPlatform] = dPlatformParse

    # NOTE reorder the column
    for sColumn in dORColumn.keys():
        if sColumn in lsTargetPrintFormatter:
            pass
        else:
            lsTargetPrintFormatter.append(sColumn)

    sPrintHeader = 'Platform\t' + '\t'.join('%s' % sTemp for sTemp in lsTargetPrintFormatter)
    sPrintFormatter = '{:<1}\t' + '\t'.join('{%s}' % sTemp for sTemp in lsTargetPrintFormatter)

    print sPrintHeader
    for sPlatform in sorted(ddPlatformParser.keys()):
        try:
            print sPrintFormatter.format(sPlatform, **ddPlatformParser[sPlatform])
            pass
        except Exception as e:
            # pprint.pprint(ddPlatformParser)
            print sPlatform
            raise
        else:
            pass


if __name__ == '__main__':
    main()