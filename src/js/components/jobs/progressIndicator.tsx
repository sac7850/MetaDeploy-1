import SLDSProgressIndicator from '@salesforce/design-system-react/components/progress-indicator';
import * as React from 'react';

import { getSteps } from '@/components/plans/progressIndicator';
import { Job } from '@/store/jobs/reducer';
import { CONSTANTS } from '@/store/plans/reducer';
import { SupportedOrgs } from '@/utils/constants';

const ProgressIndicator = ({
  job,
  supportedOrgs,
  preflightRequired,
}: {
  job: Job;
  supportedOrgs: SupportedOrgs;
  preflightRequired: boolean;
}) => {
  const steps = getSteps(supportedOrgs, preflightRequired);
  const completedSteps =
    job.status === CONSTANTS.STATUS.COMPLETE
      ? steps.slice()
      : steps.slice(0, -1);
  const errorSteps =
    job.status === CONSTANTS.STATUS.FAILED ||
    job.status === CONSTANTS.STATUS.CANCELED
      ? steps.slice(-1)
      : [];
  return (
    <SLDSProgressIndicator
      className="slds-m-top_medium"
      steps={steps}
      completedSteps={completedSteps}
      selectedStep={steps[steps.length - 1]}
      errorSteps={errorSteps}
    />
  );
};

export default ProgressIndicator;
