import { TestBed } from '@angular/core/testing';

import { WbDesignSystemService } from './wb-design-system.service';

describe('WbDesignSystemService', () => {
  let service: WbDesignSystemService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(WbDesignSystemService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
